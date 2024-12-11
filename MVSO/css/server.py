import socket

socket_server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host="172.25.224.1"
port=80
 
socket_server.bind((host,port))

socket_server.listen(5)

print("server socket listning on {}{}".format(host,port))

client_socket, client_address = socket_server.accept()

message="Congra Don Sura Goat"

client_socket.send(message.encode())

data=client_socket.recv(1024)
print(data.decode())

client_socket.close()
socket_server.close()
