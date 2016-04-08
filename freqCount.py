
myList=["Anup", "Anup",  "Anup", "Riddhima", "Riddhima", "Riddhima","Anup", "Amar", "Amar"]
def freqCount(myList):

	myDict={} # empty dictionary

	for ele in myList:  
		if ele in myDict:
			myDict[ele]+=1
		else:
			myDict[ele]=1
	return myDict

print freqCount(myList)




"""
Name 	Count

Anup  	   4

Riddhima   3
"""