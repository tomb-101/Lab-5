import socket
import threading


HOST="127.0.0.1"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7777
server.listen((HOST, port))

clients=[]
nicknames=[]

#broadcast function that sends the message to all connected clients

def sendmsg(message):
    #for every client in the current clients list
    for client in clients:
        #broadcast the message to the client
        client.send(message)

#handle function which handles the connection between clients and server and closes them upon an error

def handle(client):#
    while True:
        #if there are no errors
        try:
            #receive the message from the client
            message=client.recv(1024)
            #get the nickname of said client and display their message (only visible to server)
            print(f"{nicknames[clients.index[client]]}: {message}")
            #broadcast this to everyone
            sendmsg(message)
        
        #if there is an error on the client's end
        except:
            #get the client's index (to use later in the nicknames list)
            index=clients.index(client)

            #remove the client from the client list and close the client's connection to the session
            clients.remove(client)
            client.close()

            #get the nickname of the former client using the index and remove it from the list
            nickname=nicknames[index]
            nicknames.remove(nickname)

            #break the connection from the server to the client
            break

#receive function that is always running and waiting to receive a connection from a client
        
def receive():
    #infinite loop
    while True:
        #accept the connection between client and server and return their address
        client, address=server.accept()
        #display the connection between the server and client
        print(f"Connected with {str(address)}")
        #add the client to the list of clients
        clients.append(client)


        #send a message which tells client to enter a nickname
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024)
        #add the nickname to the nicknames list
        nicknames.append(nickname)
        
        #this is only displayed on the server
        print(f"Client's nickname is {nickname}")

        #send everyone in the chat that a new user has joined
        sendmsg(f"{nickname} has joined the chat\n".encode('utf-8'))

        #tell the person that just joined that they have connected
        client.send("You have joined the chat")


        #make the thread
        thread=threading.Thread(target=handle, args=(client,))
        #start the thread
        thread.start()


print("---Server running---")
#run the receive funtion
receive()