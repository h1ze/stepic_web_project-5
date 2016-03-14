# -*- coding: utf-8 -*-

"""

"""


def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    body = "\n".join(environ["QUERY_STRING"].split("&"))
    return body

if __name__ == '__main__':
    pass