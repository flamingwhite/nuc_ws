import os

n=0
os.chdir('./logs')
for f in os.listdir('.'):
	arr=f.split('-')
	arr[2], arr[3] = arr[3], arr[2]
	del arr[1]
	newname='-'.join(arr)
	os.rename(f, newname)
	print(f, ' ==> ', newname)
	n+=1

print(n)
