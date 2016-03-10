def application(environ, start_response):
    """Simplest possible application object"""



    resp = environ['QUERY_STRING'].split("&")
    resp = environ['QUERY_STRING'].replace("&","\n")
    resp = resp+"\r\n"

    status = '200 OK'
    response_headers = [
        ('Content-Type','text/plain'),
        ('Content-Length', str(len(resp)))
    ]
    start_response(status, response_headers)
    # resp = [item+"\r\n" for item in resp]
    # return iter([data])
    return resp