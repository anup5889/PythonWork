
from collections import OrderedDict

def highFreqEle(myList):

	return OrderedDict(sorted(freqCounter(myList).items(),key=lambda t:t[1] )).popitem()


def freqCounter(myList):
	freqDict={}

	for ele in myList:
		if ele in freqDict:
			freqDict[ele]+=1
		else:
			freqDict[ele]=1

	return freqDict


print highFreqEle(["Anup", "Anup", "Anup", "Anup", "Anup", "Anup", "Priyanka", "Priyanka", "Priyanka"])


