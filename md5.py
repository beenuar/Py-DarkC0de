
import md5, sys ,time , os

if len(sys.argv) != 2:
	print "\n\t\t Coded By Beenu Arora"
	print "Usage: ./md5gen.py <password>"
	sys.exit(1)
	
pwd = sys.argv[1]
length = len (pwd)
for i in range ( length):
	hash = md5.new()
	hash.update(pwd)
	pwd = hash.hexdigest()

print "\nYour password hash after " , length , "hashing :"
time.sleep(1)
print hash.hexdigest()
