import socket               
s = socket.socket()         
port = 12351        
host_addr = socket.gethostname()      
s.connect((host_addr, port))

while True:	
	msg = raw_input()
	s.send(msg)
	if msg == 'close':
		s.close() 
		exit()
	print s.recv(1024)

