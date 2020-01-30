'''
File: twist.py
Author: Samantha Mathis
CSC 346 Spring 2020
'''

from socket import *
import sys

my_sock = socket(AF_INET, SOCK_STREAM)

host = sys.argv[1]
file = sys.argv[2]

add = (host, 80)
my_sock.connect(add)

mesg = ('GET ' + file + ' HTTP/1.0\n'
'Host: ' + host + '\r\n\r\n')
print(mesg)

my_sock.sendall(mesg.encode())

str1 = ""
while True:
    data = my_sock.recv(1024).decode()
    str1 += data
    if data == "":
        break

print(str1)
