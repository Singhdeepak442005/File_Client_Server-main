import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 20001
BUF_SIZE = 32

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

file_name = input("Enter The File Name : ")
s.send(file_name.encode())

data = s.recv(BUF_SIZE).decode()
if data == "0x":
    print(f"Msg From Server : File Not Exists")
else:
    file = open(file_name, 'a+')
    while data:
        file.write(data)
        data = s.recv(BUF_SIZE).decode()
    file.close()
