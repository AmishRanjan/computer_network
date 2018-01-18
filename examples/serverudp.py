import socket               
 
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)        
 
port = 12348               
host = socket.gethostname()  
s.bind((host, port))        
              
 
while True:     
   msg, addr = s.recvfrom(1024)
   s.sendto("from server " + str(msg),addr)
   if msg == 'close':
      s.close()
      exit()
