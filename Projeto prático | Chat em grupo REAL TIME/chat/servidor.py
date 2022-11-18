import socket
import threading

HOST = '127.0.0.1'
PORT = 3308

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcaast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        i.send(mensagem)

def enviaMensagem(nome, sala, claent):
    while True:
        mensagem = claent.recv(1024)
        mensagem = f'{nome}: {mensagem.decode()}\n'
        broadcaast(sala, mensagem)

while True:
    claent, addr = server.accept()
    claent.send(b'#SALA#')
    sala = claent.recv(1024).decode()
    nome = claent.recv(1024).decode()

    if not sala in salas.keys():
        salas[sala] = []
    salas[sala].append(claent)
    print(f'{nome} se conectou a sala {sala}! INFO {addr}')
    broadcaast(sala, f'{nome} entrou na sala!\n')
    thread = threading.Thread(target=enviaMensagem, args=(nome, sala, claent))
    thread.start()