def maxmain():
	s=0
	l=[]
	max=-1
	n=int(input())
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		if l[i]<l[i+1]:
			s+=1
		else:
			continue
		if max<s:
			max=s
	print(max)
try:
	maxmain()
except:
	print('invalid input')
