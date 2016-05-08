
import socket , string , sys
from time import time, ctime

if len(sys.argv) != 3:
	print "\nUsage: ./honeypot.py <port> <file to save attempts>"
	print "Ex: ./honeypot.py 21 attacks.txt\n"
	sys.exit(1)
	
banner = raw_input("\nPlease Enter Banner: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(("", int(sys.argv[1])))
print "\n Scan started at " , ctime(time())
print "\n[+] Waiting for connections...\n"
s.listen(5)

while 1:
	try:
		(clientsock, clientaddr) = s.accept() 
		print "\a"*5  #Setup to beep 5 times on connection
		clienthost = clientsock.getpeername()[0]
		clientport = clientsock.getpeername()[1]
		file = open(sys.argv[2], "a")  #Logs remote ip/potrt
		print "-"*45
		print "[-] Connection attempt:",clienthost+":"+str(clientport)
		file.writelines("\n"+clienthost+":"+str(clientport))
		clientsock.send("\n"+banner+"\n\n") 
		resp = clientsock.recv(1024)
		clientsock.send("\nIllegal Access, your IP ["+clienthost+"] has been logged.\n\n")
		clientsock.close()
		file.close()
	except(KeyboardInterrupt):
		print "\n[-] Exiting:",timer()
		sys.exit(1)
	except:
		continue