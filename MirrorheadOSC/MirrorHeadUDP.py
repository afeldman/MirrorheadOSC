import socket   #for sockets
import sys  #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
 
ip = "192.168.0.200"
port = 7475
 
msg = "/mdc_layer1_preset3"
     
try :
      #Set the whole string
    s.sendto(msg, (host, port))
         
except Exception:
    print ('could nor send')
    

