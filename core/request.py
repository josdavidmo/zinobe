from cgi import escape, parse_qs


def GET(environ):
    # Returns a dictionary in which the values are lists
    request = parse_qs(environ['QUERY_STRING'])
    request = {key: request[key][0].decode('utf-8') for key in request}
    return request


def POST(environ):
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    request = parse_qs(request_body)
    request = {key: request[key][0].decode('utf-8') for key in request}
    return request
