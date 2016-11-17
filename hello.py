 #environ['QUERY_STRING'].replace("&", "\r\n")
def hello(environ, start_response):
    # бизнес-логика
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = 'Hello, world!'
    start_response(status, headers )
    return [ body ]
def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
return iter([data])
