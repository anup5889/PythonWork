"""
Counter is a datatype in python collections

"""

from collections import Counter
def counterExample(myList):

	cnt=Counter()
	for ele in myList:
		cnt[ele]+=1

	return cnt

counterEx= counterExample(["Hello", "Hello", "Hello", "Amazon", "Tree"])
print counterEx
print counterEx["Hello"]

for ele in counterEx:
	print ele


def counterExampleWithoutCounter(myList):
	freqCount={}
	for ele in myList:
		if ele in freqCount:
			freqCount[ele]+=1
		else:
			freqCount[ele]=1
	return freqCount

print counterExampleWithoutCounter(["Hello", "Hello", "Hello", "Amazon", "Tree"])

def counterE
	



