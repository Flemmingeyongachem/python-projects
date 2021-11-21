import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

message='Hello UDP server'
client_socket.sendto(message.encode('utf-8'),('127.0.0.1',12345))
data,addr=client_socket.recvfrom(4096)
print('Server says')
print(str(data))
client_socket.close()