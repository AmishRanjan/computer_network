import socket 
import thread              

port = 12351
 
Server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

host_addr = socket.gethostname()

Server_socket.bind((host_addr, port))                         

def echomsg(c, addr):
   while True:     
      msg = c.recv(1024)
      c.send(msg)
      print msg
      if msg == 'close':
	 c.close()
         Server_socket.close()
         exit() 
   
while True: 
   Server_socket.listen(15) 
   c, addr = Server_socket.accept()  
   print 'Got connection from', addr
   thread.start_new_thread(echomsg,(c, addr))   
   
   
 
