def application (environ, start_response):

    response_body = environ['QUERY_STRING'].replace("&", "\r\n")

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]
