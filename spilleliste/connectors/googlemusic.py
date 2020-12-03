# -*- coding: utf-8 -*-
try:
	from gmusicapi import Mobileclient
except ImportError:
	raise Exception('You need gmusicapi python package (pip install gmusicapi)')


def get_playlists(username, password):
	api = Mobileclient(debug_logging=False)
	api.login(username, password)

	playlists = {}
	_playlists = api.get_all_playlists()

	for playlist in _playlists:
		playlist_name = playlist['name']
		playlists[playlist_name] = api.get_shared_playlist_contents(
			playlist['shareToken'])

	for playlist_name, playlist_songs in playlists.items():
		songs = []
		for song in playlist_songs:
			song = song['track']
			s = (song['artist'], song['album'], song['title'])
			songs.append(s)
		playlists[playlist_name] = songs

	return playlists
