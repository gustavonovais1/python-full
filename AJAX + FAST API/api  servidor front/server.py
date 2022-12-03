def app(amd, start_response):
    arq = open('index.html', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'text/html')]
    start_response(status, response_headers)
    return [data]

def app2(amd, start_response):
    arq = open('login.html', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'text/html')]
    start_response(status, response_headers)
    return [data]

# gunicorn server:app -b 127.0.0.1:5002