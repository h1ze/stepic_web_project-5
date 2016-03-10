def wsgi_app(env, start_response):


  status = '200 OK'
  header = [('Content-Type', 'text/plain')]

  body = []
  for key in env['QUERY_STRING'].split('&'):
    data = key + "\n"
    body.append(data)


  start_response(status, header)
  return body