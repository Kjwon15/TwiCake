def app(environ, start_response):
    response_body = 'Hello World!'
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plan'),
                        ('Contest-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]
