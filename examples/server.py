import socket  
import threading             
 
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM) 

port = 12322              
host = socket.gethostname()  
s.bind((host, port))        
s.listen(5)               
c, addr = s.accept()        

def recvmsg():
   while True:     
      msg = c.recv(1024)
      print(msg)
      if msg == 'close':
         s.close()
         exit()

def sendmsg():
   msg = 'hello'
   while msg <> 'close':     
      msg = raw_input()
      msg = c.send(msg) 
t1 = threading.Thread(target=sendmsg)
t2 = threading.Thread(target=recvmsg)
t1.start()
t2.start()

