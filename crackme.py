#This tool extracts MD5's from a file and then searches online for cracking 
#I have used the darkc0de to crack as they have a nice lookup from other sites
#C0de is meant to be authorised pen-testing , author is not responsible for any misuse
#Every application has bugs so i you find it lemme know about it :). Follow the Just-In- Need Code

import urllib,sys,re,socket,urllib2,os,time


if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
	SysCls = 'clear'
elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
	SysCls = 'cls'
else:
	SysCls = 'unknown'

os.system(SysCls)

print "\n|---------------------------------------------------------------|"
print "| beenudel1986[@]gmail[dot]com                                  |"
print "| Hash Extractor and Online Cracker                             |"
print "|   11/2008      cracker.py                                     |"
print "|   Do Visit     www.BeenuArora.com      &        darkc0de.com  |"
print "|---------------------------------------------------------------|\n"

if len(sys.argv) !=2:
	print "\n beenudel1986[at]gmail[dot]com"
	print "\n Usage: ./crackme.py <File-name>"
	sys.exit(1)

list= sys.argv[1]
try:

	lines= open(list,'r')
except (IOError):
	print " \n\nSite List Missing ..Exiting :("
	sys.exit(0)

for line in lines:
 	line=line[:-1]
	socket.setdefaulttimeout(10)
	file=open ('hash.txt' , 'a')
	hash=re.findall("[a-f0-9]"*32,line)
	for hashes in hash:
		print "\n [-] Searching for hash "+hashes
		try:
			time.sleep(7.0)
			url ="http://www.darkc0de.com/cgi-bin/md5lookup.py?hash="+hashes
			site = urllib.urlopen(url).readlines()
			for response in site:
				if re.search("==", response):
					response=response.replace("<hr>","").replace('[!]',"").replace('<br><br></td></tr></table>',"")
					print "\n Password of hash " ,response
					file.write('\t'+response+'\n')
		except(urllib2.URLError, socket.timeout, socket.gaierror, socket.error): 
			pass 
		except(KeyboardInterrupt): 
			pass 
