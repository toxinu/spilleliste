# -*- coding: utf-8 -*-

def search(artist, album, title):
	query = "%s+%s+%s" % (artist, album, title)
	return u"https://www.youtube.com/results?search_query=%s" % query
