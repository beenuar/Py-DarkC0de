#!/usr/bin/env python
#Randomly scans for ftp servers and checks anonymous login.
#If login successful it will show ip and server response
#to channel.

#http://www.darkc0de.com
#d3hydr8[at]gmail[dot]com

#Verbose mode will print out ftp servers even if 
#anonymous is not allowed.
#Set this to 0 to disable
verbose = 1

import sys, socket, string, time, ftplib, random, os

if len(sys.argv) != 5:
	print "Usage: ./ftpanonbot.py <host> <port> <nick> <channel>"
	sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
NICK = sys.argv[3]
CHAN = sys.argv[4]
readbuffer = ""

s=socket.socket( )
s.connect((HOST, PORT))
print "\n[+] Connecting:",HOST,PORT
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (NICK, NICK, NICK))
print "[+] Nick:",NICK
print "[+] Joining Chan:",CHAN
s.send("JOIN :%s\r\n" % CHAN)
s.send("PRIVMSG %s :%s\r\n" % (CHAN, "[+] FTP Scanbot Loaded"))
if verbose == 1:
	print "[+] Verbose Mode: ON"
else:
	print "[-] Verbose Mode: OFF"

def rand():
	a = random.randrange(255) + 1
	b = random.randrange(255) + 1
	c = random.randrange(255) + 1
	d = random.randrange(255) + 1
	ip = "%d.%d.%d.%d" % (a,b,c,d)
	return ip

def scan():
	
	ipaddr = rand()

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(15)
		s.connect((ipaddr, 21))
		s.close()
		return ipaddr
	except socket.error:
		pass
					
pid = os.fork()
if pid:
	print "[+] Starting Scan..."
	while 1:
		#Change this time as needed (secs)
		time.sleep(10)
		try:
			ipaddr = scan()
			welcome = ""
			if ipaddr:
				print "\n[+] Checking anonymous login:",ipaddr
				s.send("PRIVMSG %s :%s%s\r\n" % (CHAN, "[+] Checking anonymous login: ",ipaddr+":21"))
				ftp = ftplib.FTP(ipaddr)
				welcome = ftp.getwelcome()
				print "[+] Response:",welcome
				ftp.login()
				ftp.retrlines('LIST')
				print "\t[!] Anonymous login successful:",ipaddr
				s.send("PRIVMSG %s :%s%s\r\n" % (CHAN, "[!] FTP Anonymous Login: ",ipaddr+":21"))
				s.send("PRIVMSG %s :%s%s\r\n" % (CHAN, "Running: ",welcome))
				ftp.quit()
		except (ftplib.all_errors), msg: 
			print "[-] An error occurred:",msg,"\n"
			if verbose != 0 and welcome != "":
				s.send("PRIVMSG %s :%s\r\n" % (CHAN, "[-] Anonymous login unsuccessful"))
				s.send("PRIVMSG %s :%s%s\r\n" % (CHAN, "Running: ",welcome))

else:
	while 1:
		readbuffer=readbuffer+s.recv(1024)
    		temp=string.split(readbuffer, "\n")
    		readbuffer=temp.pop( )
    		for line in temp:
        		line=string.rstrip(line).split(line)
			#print line	
        		if line[0].find("PING") != -1:
				print "\nSending PONG\n"
          			s.send("PONG %s\r\n" % HOST)
