# -*- coding: utf-8 -*-

import requests


def search(artist, album, title):
    res = None
    request = "%s %s" % (artist, title)

    r = requests.get('http://ws.spotify.com/search/1/track.json?q=%s' % request)

    try:
        data = r.json()
    except ValueError:
        return False

    if data:
        for track in data['tracks']:
            if res is not None:
                if res['popularity'] < track['popularity']:
                    res = track
            else:
                res = track

    if res is not None:
        return res['href']
    else:
        return False
