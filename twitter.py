T=int(raw_input())
for i in range(T):
	height=1
	n=int(raw_input())
	for i in range(1,n+1):
		if i%2==0:
			height+=1
		else:
			height*=2

	print height

