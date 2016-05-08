import sys,os,string
print "\n\t\t~~~~~~~~~~~~~~~~~~~~~~ A small Virus ~~~~~~~~~~~~~~~"
print "\t\t~~~~~~~~~~~~~~~~~~~~~~~~~Coded By : Beenu Arora  ~~~~~~~~~~~~~~"

if sys.platform[:3] == 'win':
	file=open('virus.exe' , 'w')
	file.write("01001011000111110010010101010101010000011111100000")
	file.close
	print (" \n Virus File created \n")
	info=os.stat(r'virus.exe')
	print ("Statistics of Virus are " +str(info))
	raw_input()
	print (" \n Executing Virus...")
	os.system('virus.exe')
else:
	print("Can't Say for other platforms ")
	raw_input()

