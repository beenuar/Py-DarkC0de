#Attempts to crack hash against any givin wordlist.


import md5, sys

if len(sys.argv) != 3:
	print " \n beenudel1986@gmail.com"
	print "\n\nUsage: ./md5crack.py <hash> <wordlist>"
	sys.exit(1)
	
pw = sys.argv[1]
wordlist = sys.argv[2]
try:
  words = open(wordlist, "r")
except(IOError): 
  print "Error: Check your wordlist path\n"
  sys.exit(1)
words = words.readlines()
print "\n",len(words),"words loaded..."
file=open('hash.txt','a')
for word in words:
	hash = md5.new(word[:-1])
	value = hash.hexdigest()
	if pw == value: 
		print "Password is:",word,"\n"
		file.write("\n Cracked Hashes\n\n")
		file.write(pw+"\t\t")
		file.write(word+"\n")




	
	



