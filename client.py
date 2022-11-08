from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))  # connect to server (block until accepted)
print('Digite dois numeros e uma operação(add, multiply, subtract ou divide) separados por espaço ou fim para '
      'encerrar o programa')
while True:
    msg = input()
    if msg == "fim" or msg == "FIM" or msg == "Fim":
        break
    s.send(str.encode(msg))  # send some data
    data = s.recv(1024)  # receive the response
    print(bytes.decode(data))  # print the result
s.close()  # close the connection
