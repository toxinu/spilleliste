# -*- coding: utf-8 -*-


class Track(object):
    def __init__(self, name, infos):
        self.name = name
        self.infos = infos


class Album(object):
    def __init__(self, name, infos):
        self.name = name
        self.tracks = []
        self.infos = infos

    def add_track(self, track, track_infos={}):
        #if not track in [ __track.name for __track in self.tracks ]:
        self.tracks.append(Track(track, track_infos))


class Artist(object):
    def __init__(self, name, infos):
        self.name = name
        self.albums = []
        self.tracks = self.get_tracks()
        self.infos = infos

    def add_track(self, album, track, album_infos={}, track_infos={}):
        if album not in [ __album.name for __album in self.albums ]:
            _album = Album(album, album_infos)
            _album.add_track(track, track_infos)
            self.albums.append(_album)
        else:
            _album = [ __album for __album in self.albums if __album.name == album ][0]
            _album.add_track(track, track_infos)

    def get_tracks(self):
        res = []
        for album in self.albums:
            res.append(album.get_tracks())
        return res


class Playlist(object):
    def __init__(self, name, external_uri='#'):
        self.name = name
        self.artists = []
        self.external_uri = external_uri
        self.tracks = self.get_tracks()

    def add_track(self, artist, album, track, artist_infos={}, album_infos={}, track_infos={}):
        if artist not in [ __artist.name for __artist in self.artists ]:
            _artist = Artist(artist, artist_infos)
            _artist.add_track(album, track, album_infos, track_infos)
            self.artists.append(_artist)
        else:
            _artist = [ __artist for __artist in self.artists if __artist.name == artist ][0]
            _artist.add_track(album, track, album_infos, track_infos)

    def get_tracks(self):
        res = []
        for artist in self.artists:
            res.append(artist.get_tracks())
        return res

    def get_artists(self):
        return [ __artist for __artist in self.artists ]

    def set_external_uri(self, tracks):
        uri = tracks[0]
        for track in tracks[1:]:
            uri += u',%s' % track
        self.external_uri = 'spotify:trackset:PREFERED:%s' % uri
