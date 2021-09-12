# Access from outside of the network might need port forwarding from host-side 

# import socket module
from socket import *
import sys # In order to terminate the program


# Using IPv4, TCP socket (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket, associate port number
port = 6789
address = "0.0.0.0"
serverSocket.bind((address, port))

# Wait for client to request TCP connection
serverSocket.listen(1)

while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1] # parsing HTTP request
        f = open(filename[1:])
        outputdata = f.read()


        #Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK'
        for i in range(0, len(header)):
            connectionSocket.send(header[i].encode())
        connectionSocket.send("\r\n\n".encode())


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print('404 Not Found')

        #Close client socket
        connectionSocket.close()

    serverSocket.close()
    sys.exit() # Terminate the program after sending the corresponding data
