# client.py
from socket import *
from time import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 11559))
print("Connected to the Server")
while True:
    received = client.recv(1024).decode()
    print("Server:" ,received)
    data = input("Client: ")
    client.send(bytes(data +" "+ctime(), "utf-8"))
    print("Succesfully Send")


client.close()
