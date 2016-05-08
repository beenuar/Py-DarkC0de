# A simple Port Scanner

import sys,socket

if len(sys.argv) <4:
	print "\n beenudel1986[at]gmail[dot]com"
	print "\n\nusgae: ./portscan.py <host> <startport> <end port>"
	print "\n Example: portscan.py www.wizom.com 1 1000"
	sys.exit(0)

host=sys.argv[1]
start=sys.argv[2]
end =sys.argv[3]

for port in range (int(start),int(end)):
	try:
		print "\n[-] Scanning port",port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((socket.gethostbyname(host), int(port)))
		print "\n Found Open Port ",port
		s.close()
	except:
		pass

