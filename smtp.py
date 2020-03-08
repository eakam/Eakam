import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"
mysocket.connect((server_ip, 25))
data = mysocket.recv(1024)
print data
while(True):
	data1 = raw_input()
	data1 = data1+'\n'
	mysocket.send(data1)
	b = mysocket.recv(1024)
	print b
