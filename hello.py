def app (environ, start_response):
    response_status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(response_status, response_headers)
    response_body = '\r\n'.join(environ['QUERY_STRING'].split('&'))
    return response_body
