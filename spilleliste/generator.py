# -*- coding: utf-8 -*-

import os
import requests
import codecs

from spilleliste.core import Playlist
from spilleliste.core import Artist
from spilleliste.core import Album
from spilleliste.core import Track

from spilleliste.externals import googleimage
from spilleliste.externals import spotify
from spilleliste.externals import youtube

from jinja2 import Template


def run(raw_playlists, args, template_name="default", template_uri=False):
	# Playlists
	playlists = []

	print('=> Building playlists...')
	print('=> Retrieving externals uri (could be long)...')
	for playlist_name, tracks in raw_playlists.items():
		playlist = Playlist(playlist_name)
		playlist_external_uri = []

		for track in tracks:
			artist = unicode(track[0])
			album = unicode(track[1])
			title = unicode(track[2])
			track_infos = {}

			provider = "unknown"
			external_uri = ""
			
			if not args.get('--no-spotify'):
				provider = "spotify"
				external_uri = spotify.search(artist, album, title)

			if not args.get('--no-youtube'):
				if not external_uri:
					provider = "youtube"
					external_uri = youtube.search(artist, album, title)
				else:
					playlist_external_uri.append(external_uri.split(':')[-1])

			track_infos = {u'provider': provider, u'url': external_uri}
			playlist.add_track(artist, album, title, track_infos = track_infos)

		if playlist_external_uri:
			playlist.set_external_uri(playlist_external_uri)
		playlists.append(playlist)

	# Get backgrounds
	backgrounds = []
	if not args.get('--no-background'):
		print('=> Retrieving externals images (could be long)...')
		backgrounds = googleimage.search(playlists, int(args.get('--nb-background', 5)))

	if not args.get('--template-url'):
		page_template = requests.get('https://raw.github.com/toxinu/spilleliste/master/one_page.html').text
	elif args.get('--template-url'):
		page_template = requests.get(args.get('--template-url')).text

	template = Template(page_template)
	output_content = template.render(playlists=playlists, backgrounds=backgrounds)

	output_file_name = '%s/spilleliste.html' % os.getcwd()
	output_file = codecs.open(output_file_name, mode='w', encoding='utf-8')
	output_file.write(output_content)

	print(' :: Done (%s)' % output_file_name)
