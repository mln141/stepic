 #environ['QUERY_STRING'].replace("&", "\r\n")
def hello(environ, start_response):
 data = environ['QUERY_STRING'].replace("&", "\r\n").replace("?", "\r\n" #b"Hello, World!\n"
 start_response("200 OK", [
  ("Content-Type", "text/plain"),
  ("Content-Length", str(len(data)))
 ])
 return iter([data])
