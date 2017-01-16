import os

n=0
os.chdir('./logs')
for f in os.listdir('.'):
	arr=f.split('-')
	arr[1], arr[2] = arr[2], arr[1]
	newname='-'.join(arr)
	os.rename(f, newname)
	print(f, ' ==> ', newname)
	n+=1

print(n)
