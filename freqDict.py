'''
function which takes a list and a number 
and returns the most frequent n numbers
'''
a=[1,1,2,3,3,3,3,4,5,6]
def frequencyCounterOfList(myList,n):
	print(myList)
	freqDict={}
	sorted_list=[]
	for i in myList:
		if i in freqDict:
			freqDict[i]+=1
		else:
			freqDict[i]=1
	print freqDict
''' logic to reverse a Dictory and return it in the form of list of tuples'''

	sorted_list = [(k,v) for v,k in sorted(
		[(v,k) for k,v in freqDict.items()], reverse=True 
		)]
   	return sorted_list[:n]

##################################################

print(frequencyCounterOfList(a,2))











