import random 
from socket import * 

# creating a UDP Socket 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# assigning IP address and port number to socket 
serverSocket.bind(('', 12000))

while True:
	# generate a random number in the range of 0 to 10 
	rand = random.randint(0, 10)
	# receive the client packet along the address it is coming from 
	message, address = serverSocket.recvfrom(1024)
	# capitalize the message from the client 
	message = message.upper()
	# if rand is less than 4, we consider the packet lost and do not respond 
	if rand < 4:
		continue
	# otherwise, the server responds 
	serverSocket.sendto(message, address)
		