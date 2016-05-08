import thread, time , os ,sys

def counter(id , count,):
	for i in range (count):
		os.system('ping 127.0.0.1 /t')
for i in range (100):
	thread.start_new_thread(counter , (i,30,))

time.sleep(1)
print ' Thread Over..!!'