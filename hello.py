import urlparse

def application(env, start_response):
    data = urlparse.parse_qsl(env["QUERY_STRING"], True)

    result = ""

    for key, value in data:
        result += key + "=" + value + "\n"

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)

    return result