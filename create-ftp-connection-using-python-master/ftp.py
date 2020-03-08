
import sys
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = raw_input("Enter the remote ip:")
mysocket.connect((server_ip, 21))
data1 = mysocket.recv(1024)
print data1
while(True):
	data = raw_input()
	mysocket.send("%s\n"%data)
	if(data == "PASV"):
		d = mysocket.recv(1024)
		print d
		a = []
		a = d.split(",")
		f = int(a[-2])
		x = a[-1].split(")")		
		h = int(x[0])
		e = (f*256)+h
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(("10.1.0.101", e))
		data2 = raw_input()
		sock.send("%s\n"%data2)
	b = mysocket.recv(4096)
	print (b.decode("utf-8"))





	
	
	


		
