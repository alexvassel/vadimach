from bottle import route, run, request, HTTPResponse


@route('/')
def index():
    if request.headers.get('X-Header'):
        return 'hello world'
    raise HTTPResponse('Internal server error', status=500, headers={})


run(host='localhost', port=8888)
