import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 20001
BUF_SIZE = 32

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

s.listen(1)
conn, addr = s.accept()
print ("Connection Address is : " , addr)

file_name = conn.recv(BUF_SIZE).decode()
print(f"File Name : {file_name}")

try:
    with open(file_name, 'r') as file:
        data = file.read()
        conn.send(data.encode())
except:
    conn.send("0x".encode())

s.close()