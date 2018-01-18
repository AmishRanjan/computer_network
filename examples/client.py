import sys
import socket               
import threading 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
port = sys.argv[2]              
host = sys.argv[1]              
#host = socket.gethostname() 
s.connect((host, port))
'''def sendmsg():
	msg = "hello"
	while(msg <> "close"):
		msg = raw_input()
		s.send(msg)
	s.close() '''
 
#def recvmsg():
msg = s.recv(1024)
print(msg)

#t1 = threading.Thread(target=sendmsg)
#t2 = threading.Thread(target=recvmsg)
#t1.start()
#t2.start()

