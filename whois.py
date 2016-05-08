import urllib, sys, re

if len(sys.argv) != 2:
	print "\n beenudel1986[at]gmail[dot]com"
	print "\n Usage: ./whois.py <domain-name>\n"
	sys.exit(1)

name = sys.argv[1]
url = "http://reports.internic.net/cgi/whois?whois_nic=" +name +"&type=domain"

site = urllib.urlopen(url).readlines()

for line in site:
	if re.search("Domain Name:", line):
		print "\n" , line ,"\n"
	if re.search("Registrar:", line):
		print line ,"\n"
	if re.search("Name Server:", line):
		print line , "\n"
	if re.search("Whois Server:", line):
		print line , "\n"
	if re.search("Referral URL:", line):
		print line, "\n"
	if re.search("Status:", line):
		print line, "\n"
	if re.search("Updated Date:", line):
		print line, "\n"
	if re.search("Creation Date:", line):
		print line, "\n"
	if re.search("Expiration Date:", line):
		print line, "\n"