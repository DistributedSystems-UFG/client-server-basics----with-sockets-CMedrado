from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))  # connect to server (block until accepted)
msg = "3 4 add"
s.send(str.encode(msg))  # send some data
msg = "3 4 subtract"
s.send(str.encode(msg))  # send some data
msg = "3 2 subtract"
s.send(str.encode(msg))  # send some data
msg = "3 4 multiply"
s.send(str.encode(msg))  # send some data
msg = "3 5 multiply"
s.send(str.encode(msg))  # send some data
data = s.recv(1024)  # receive the response
print(bytes.decode(data))  # print the result
s.close()  # close the connection
