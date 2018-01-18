import socket               
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
port = 12348               
host = socket.gethostname() 
msg = raw_input()
s.sendto(msg, (host, port))
msg , addr = s.recvfrom(1024)
print(msg)
s.close()  
