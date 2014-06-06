from __future__ import print_function
import sys
import json

HEADER = {'User-Agent': 'RealTimeWeb Facebook library for educational purposes'}
PYTHON_3 = sys.version_info >= (3, 0)

if PYTHON_3:
    import urllib.error
    import urllib.request as request
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus

