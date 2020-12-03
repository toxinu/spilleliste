# -*- coding: utf-8 -*-

import random
import requests


def search(playlists, nb_background=5):
    artists = []
    for playlist in playlists:
        artists += playlist.get_artists()

    background_found = 0
    backgrounds = []
    while background_found < nb_background:
        for artist in random.sample(artists, nb_background - background_found):
            search_terms = u'%s %s music' % (artist.name, random.choice(artist.albums).name)
            #print('     - %s ' % search_terms)
            r = requests.get('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&imgsz=xxlarge' % search_terms.replace(' ', '+'))
            data = r.json()
            try:
                backgrounds.append(data['responseData']['results'][0]['url'])
                background_found += 1
            except Exception as err:
                artists.remove(artist)
                break
    return backgrounds
