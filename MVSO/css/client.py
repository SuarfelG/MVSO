import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host="172.25.224.1"
port=80

message="Hello Don"

client_socket.connect((host,port))
client_socket.send(message.encode())

data = client_socket.recv(1024)

print(data.decode())


client_socket.close()
