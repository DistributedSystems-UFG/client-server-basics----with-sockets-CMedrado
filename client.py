from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
s.send(str.encode('3 4 add'))  # send some data
s.send(str.encode('3 4 subtract'))  # send some data
s.send(str.encode('3 2 subtract'))  # send some data
s.send(str.encode('3 4 multiply'))  # send some data
s.send(str.encode('3 5 multiply'))  # send some data
data = s.recv(1024)     # receive the response
print (bytes.decode(data))            # print the result
s.close()               # close the connection
