import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create the client socket
print("Choose Port: ")
port=input() #this should be 7777 in accordance with the server.py file
client.connect(("localhost", port))
done=False
while not done: #loops until a certain message is received
    client.send(input("Message: ").encode('utf-8')) #requests the connection for the user to provide a message
    msg=(client.recv(1024).decode('utf-8')) #encodes the message
    if msg == "--quit":
        done=True #ends the loop (could also be performed with "break")
    else:
        print(msg) #if message is not the quit command, display the message

client.close() #upon ending the loop, end the connection

#
# this is sample code used to connect to a server to communicate with it
# and is only meant for testing purposes.
#