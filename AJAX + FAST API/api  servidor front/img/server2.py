def app4(amd, start_response):
    arq = open('img1.jpg', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'multipart/jpg')]
    start_response(status, response_headers)
    return [data]

def app5(amd, start_response):
    arq = open('img2.jpg', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'multipart/jpg')]
    start_response(status, response_headers)
    return [data]

def app6(amd, start_response):
    arq = open('img3.jpeg', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'multipart/jpeg')]
    start_response(status, response_headers)
    return [data]

def app7(amd, start_response):
    arq = open('img4.jpeg', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'multipart/jpeg')]
    start_response(status, response_headers)
    return [data]

def app8(amd, start_response):
    arq = open('img5.jpg', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'multipart/jpg')]
    start_response(status, response_headers)
    return [data]

def app9(amd, start_response):
    arq = open('img6.jpeg', 'rb')
    data = arq.read()
    status = '200 OK'
    response_headers = [('content-type', 'multipart/jpeg')]
    start_response(status, response_headers)
    return [data]
