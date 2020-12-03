Spilleliste
===========

Spilleliste read your favorite music player playlist and generate for you a simple but beautiful html page to share with your friends with all the Spotify links (Youtube fallback) you want.  
Music must be share.

You can easily upload it on a Dropbox or Github page.  
This is an `example`_.

Music players supported:

- Google Music
- iTunes (OSX)
- Write your own !

You can write more page template, it's Jinja template engine.

Installation
------------

- via `pip`

::

    pip install spilleliste

- via `easy_install`

::

    easy_install spilleliste

Usage
-----

::

  spilleliste --help
  Spilleliste, share your beautiful playlists.

  Usage:
    spilleliste googlemusic --username <username> --password <password> [options]
    spilleliste itunes [options]
    spilleliste -h | --help
    spilleliste -v | --version

  Options:
    --no-spotify                  Disable Spotify URI
    --no-youtube                  Disable Youtube URI
    --no-background               Disable background images
    --nb-background=<number>      Number of background [default: 5]
    --template-url=<url>          Template url
    -d, --debug                   Show debug
    -h, --help                    Show help
    -v, --version                 Show version

Thanks
------

Thanks to `backstretch`_, `requests`_, `jinja2`_, `docopt`_, `Dave Bayer`_.
Design by `Mylenela`_.

.. _example: http://dl.dropbox.com/u/79447684/spilleliste.html
.. _backstretch: http://srobbin.com/jquery-plugins/backstretch/
.. _requests: http://docs.python-requests.org/
.. _jinja2: http://jinja.pocoo.org/
.. _docopt: http://docopt.org/
.. _Dave Bayer: http://www.math.columbia.edu/~bayer/Python/iTunes/iTunes.html
.. _Mylenela: http://mylenela.fr/