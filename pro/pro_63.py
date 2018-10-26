 def pro_63():
	s=input('Enter :')
	n=len(s)
	cur_len=1
	max_len=1
	prev_ind=0
	i=0
	visited=[-1]*256
	visited[ord(s[0])]=0
	for i in range(1,n):
		prev_ind=visited[ord(s[i])]
		if prev_ind==-1 or i-cur_len >prev_ind :
			cur_len+=1
		else :
			if cur_len>max_len :
				max_len=cur_len
			cur_len=i-prev_ind
		visited[ord(s[i])]=i
	if cur_len>max_len:
		max_len=cur_len
	return max_len
pro_63()
