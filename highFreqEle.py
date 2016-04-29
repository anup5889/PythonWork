
from collections import OrderedDict

def highFreqEle(myList):
	length=len(freqCounter(myList))
	n=2
	print OrderedDict(sorted(freqCounter(myList).items(),key=lambda t:t[1] ))
	return OrderedDict(sorted(freqCounter(myList).items(),key=lambda t:t[1] )).popitem()


def freqCounter(myList):
	freqDict={}

	for ele in myList:
		if ele in freqDict:
			freqDict[ele]+=1
		else:
			freqDict[ele]=1

	return freqDict

def highFreqNEle(myList, n):
	myOrderedDict= OrderedDict(sorted(freqCounter(myList).items(),key=lambda t:t[1] ))
	myList=[]
	for i in range(n):
		myList.append(myOrderedDict.popitem())

	return myList



print highFreqEle(["Anup", "Anup", "Anup", "Anup", "Anup", "Anup", "Priyanka", "Priyanka", "Priyanka"])
print highFreqNEle(["Anup", "Anup", "Anup", "Anup", "Anup", "Anup", "Priyanka", "Priyanka", "Priyanka","Anushka", "Anushka", "Anushka",\
	"Amisha", "Amisha"], 3)


