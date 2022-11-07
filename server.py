from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))  # -
s.listen(1)  # -
msg = ''
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:  # forever
    data = conn.recv(1024)  # receive data from client
    msg = data.decode()
    if not data: break  # stop if client stopped
    tipo = msg.split()
    if tipo[2] == "add":
        result = float(tipo[0]) + float(tipo[1])
    elif tipo[2] == "subtract":
        result = float(tipo[0]) - float(tipo[1])
    elif tipo[2] == "multiply":
        result = float(tipo[0]) * float(tipo[1])

    output = str(result)
    conn.send(str.encode(output))  # return sent data plus an "*"
conn.close()  # close the connection
