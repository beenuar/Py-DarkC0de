import sys

def convert(format, fname):
	for line in open(fname, 'rb').readlines():
		if format == 'todos':
			if line[-1:]=='\n' and line[-2:-1] !='\r':
				line=line[-1:]='\r\n'
			
		elif format == 'tolinux':
			if line[-2:]=='\r\n':
				line=line[:-2] +'\n'

print " \n\nUnix to Dos and Dos To Linux file Convertor"
print " \n\t beenudel1986[at]gmail[dot]com "

print " Usage : ./convertor.py <ToDos Or ToLinux > <filename> "

if len(sys.argv) == 3 :
	convert ( sys.argv[1] , sys.argv[2] )
	print " Converted " , sys.argv[2]
else:
	print " Usage : ./convertor.py <ToDos Or ToLinux > <filename> "

