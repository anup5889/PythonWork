
import collections

def frequencyCounter(myString):
	#go through the string 
	#create a dictionary and key as a char of string 
	# value is the frequency of the char
	
	freqCount=collections.OrderedDict()

	for char in myString:
		if char in freqCount:
			freqCount[char]+=1
		else: 
			freqCount[char]=1

	#return freqCount

	for ele in freqCount:
		if freqCount[ele]==1:
			return ele



print frequencyCounter("swiss")

