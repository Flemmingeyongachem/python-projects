import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',12345))
payload='Hey Server'

try:
    while 1:
        client_socket.send(payload.encode('utf-8'))
        data=client_socket.recv(1024)
        print(str(data))
        more=input('want to send more data to the server?')
        if more.lower()=='y':
            payload=input('Enter payload')
        else:
            break
except KeyboardInterrupt:
    print('Exited by user')
client_socket.close()
