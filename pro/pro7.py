import math
def main():
	n=int(input())
	while(n!=0):
		l=math.sqrt(n)
		if l==int(l):
			print(int(l))
			break
		else:
			n=n-1
	if n==0:
		print('no')
    
try:
  main()
except:
  print('invalid')
