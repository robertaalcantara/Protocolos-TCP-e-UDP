import socket               # Import socket module
import time

#s = socket.socket()         # Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
host = "123.123.123.123" # Get local machine name
port = 54321                 # Reserve a port for your service.

s.connect((host, port))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
f = open('arquivo.txt','rb')
l = f.read(946)
while (l):
    s.send(l)
    #time.sleep(0.1)
    l = f.read(946)
f.close()
print ("Done Sending")
s.shutdown(socket.SHUT_WR)
s.close()
