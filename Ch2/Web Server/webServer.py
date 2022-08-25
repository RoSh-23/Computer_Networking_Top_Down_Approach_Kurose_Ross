from socket import * 
import sys

# preparing the socket 
serverPortNumber = 80
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPortNumber))
serverSocket.listen(1) # waiting for a request 
print('Ready to serve...')

while True:
	connectionSocket, addr = serverSocket.accept()
	print('Request accepted from (address, port) tuple: %s' %(addr,))
	try:
		# Receive the message and check the file name 
		message = connectionSocket.recv(2048).decode()
		filename = message.split()[1]
		f = open(filename[1:], 'r')
		outputdata = f.read()

		print("File found.")
		# returns the header line indicating that the file was found 
		headerLine = "HTTP/1.1 200 OK\r\n"		
		connectionSocket.send(headerLine.encode())
		connectionSocket.send("\r\n".encode())


		# send the file 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		

		# Terminates the connection 
		print("File sent.")
		connectionSocket.close()			

	except	IOError:
		print('Warning: file not found.')

		# return the error header to the browser
		errHeader = "HTTP/1.1 404 Not Found\r\n"
		connectionSocket.send(errHeader.encode())
		connectionSocket.send("\r\n".encode())

		# open and send the error page to the browser 
		ferr = open("notfound.html", "r")
		outputerr = ferr.read()

		for i in range(0, len(outputerr)):
			connectionSocket.send(outputerr[i].encode())
		connectionSocket.send("\r\n".encode())
		
		# terminates the connection 
		print("Error message sent.")
		connectionSocket.close()

	# Closes the application 		
	serverSocket.close()
	sys.exit()
