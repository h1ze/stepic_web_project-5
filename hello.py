# -*- coding: utf-8 -*-

import urlparse


def app(env, start_response):
    code = '200 OK'
    headers = (
        ('Content-Type', 'text/plain'),
    )
    start_response(code, headers)
    body = urlparse.parse_qsl(env['QUERY_STRING'], 1)
    body = '\n'.join('{:s}={:s}'.format(i[0], i[1]) for i in body)
    return body