 #environ['QUERY_STRING'].replace("&", "\r\n")
def wsgi_application(environ, start_response):
    # бизнес-логика
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = 'Hello, world!'
    start_response(status, headers )
    return [ body ]
