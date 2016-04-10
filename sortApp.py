S="BANANA"
S=list(S)
print(S)

kevinCount=0
stuartCount=0

for ele in S:
	if ele in ('A','E','I', 'O', 'U'):
		print ele
		kevinCount+=1
		print kevinCount
	else:
		stuartCount+=1

print kevinCount
print stuartCount




