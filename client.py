import socket
from _thread import start_new_thread

client = socket.socket()

client.connect(('192.168.51.238',3000))

data = client.recv(1024)
print('Сообщение в бинарном виде', data)
print('входящие сообщения ', data.decode())

message = 'Привет,сервер!'
data = message.encode()
client.send(data)

def getMessages():
    while True:
        data = client.recv(1024)
        print('', data.decode())
        if data.decode()=='Закрывай!' :
            break
    client.close()

start_new_thread(getMessages,())

while True:
    message = input('Введите сообщение ')
    data = message.encode()
    client.send(data)
    if data.decode()=='Закрывай!' :
        break
client.close()