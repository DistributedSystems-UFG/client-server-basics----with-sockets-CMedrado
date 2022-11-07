from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))  # -
s.listen(1)  # -
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:  # forever
  data = conn.recv(1024)  # receive data from client
  if not data: break  # stop if client stopped
  tipo = data.split()
  if tipo[2] == "add":
    result = float(tipo[1]) + float(tipo[2])
  if tipo[2] == "subtract":
    result = float(tipo[1]) - float(tipo[2])
  if tipo[2] == "multiply":
    result = float(tipo[1]) * float(tipo[2])
  else:
    result = 'invalid input'
  print(bytes.decode(result))
  conn.send(str.encode(bytes.decode(result) + "*"))  # return sent data plus an "*"
conn.close()  # close the connection
