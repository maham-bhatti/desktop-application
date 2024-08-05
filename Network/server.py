from socket import *
from time import *
server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost", 11559))
server.listen()
print("Server is Listening at 11559")
connection, address = server.accept()
print("Connection is build with the Client")

while True:
    data = input("Server: ")
    connection.send(bytes(data +" " +ctime(), "utf-8"))
    print("Succesfully Send")
    received = connection.recv(1024).decode()
    print("Client: " ,received)
 


connection.close()