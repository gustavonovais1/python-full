import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(5)

while True:
    novoSock, _ = sock.accept()
    mensagem = novoSock.recv(1024).decode()
    print(mensagem)
    novoSock.send(b'OK!')