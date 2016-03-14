# -*- coding: utf-8 -*-

"""

"""

try:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
except ImportError:
    from urllib import urlencode
    from urllib2 import Request, urlopen


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
    values = {'text': 't', 'title': 't'}
    # values = {'text': 't', 'question': '1'}
    data = urlencode(values).encode()
    # data = None
    req = Request('http://127.0.0.1:8000/question/1/', data, headers)
    req = Request('http://127.0.0.1:8000/ask/', data, headers)
    response = urlopen(req)
    print(response.read())
