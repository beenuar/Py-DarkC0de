import sys,os
from _winreg import *

print "\n Registry Tweekers"
print "\n beenudel1986[at]gmail[dot]com"

print "\t\t\n 1. Disable Shutdown"
print "\t\t\n 2. Disable Rub"
print "\t\t\n 3. Enable CD-Autorun"
print "\t\t\n 4. Disable Task Manager"
print "\t\t\n 5. Add Python to start-up"

choice =raw_input("\t\t\n Enter your choice\t\t\n")
if choice =="1":
	aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
	aKey = OpenKey(aReg, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer", 0, KEY_SET_VALUE)
	SetValueEx(aKey,"NoClose",1, REG_DWORD, 0)
	CloseKey(aKey)
if choice =="2":
	aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
	aKey = OpenKey(aReg, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer", 0, KEY_SET_VALUE)
	SetValueEx(aKey,"NoRun",1, REG_DWORD, 0)
	CloseKey(aKey)
if choice =="3":
	aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
	aKey = OpenKey(aReg, r"SYSTEM\CurrentControlSet\Services\Cdrom", 0, KEY_SET_VALUE)
	SetValueEx(aKey,"AutoRun",1, REG_DWORD, 1)
	CloseKey(aKey)
if choice =="4":
	aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
	aKey = OpenKey(aReg, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_SET_VALUE)
	SetValueEx(aKey,"Directory",1, REG_SZ, current_directory + "\\pics")
	CloseKey(aKey)

if choice =="5":
	path=raw_input("\t\t\n Enter the Application Complete path\n")
	aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
	aKey = OpenKey(aReg, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_SET_VALUE)
	SetValueEx(aKey,"Python",1, REG_SZ, path + "\\python.exe")
	CloseKey(aKey)

else:
	print "Wrong Choice"
	print "Exiting...!"
	sys.exit(0)

