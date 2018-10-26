def pro_57():
	x,y=(map(str,input().split()))
	ss=list(x)
	s=list(y)
	k=0
	for i in range(k,len(ss)-1):
		a=ss[i]+ss[i+1]
		for j in range(k,len(s)-1):
			b=s[j]+s[j+1]
			if a==b:
				print("yes")
				return
	print("no")
pro_57()
