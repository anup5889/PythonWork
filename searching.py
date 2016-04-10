'''
this program provides different searching algos
1. Linear search
'''
'''
def linearSearch(myList,num_to_search):
	for index,element in enumerate(myList):
		if(element==num_to_search):
			print("%d found at %d"%(num_to_search, index))


#linearSearch(a,5)


'''
'''
binary search

to track the middle element 

start_index
end_index

loop through the myList
	see in the middle if the element is present
	if element is present in middle:
		element found and exit()
	if element>the middle element:
		element is presenet in the later part of the myList
	if element<the middle element 
		element is present in the earlier part of the myList


'''

'''
binary search requires the list to be sorted

'''
def binarySearch(myList,num_to_search):
	start=0
	last=len(myList)-1
	
	found=False
	while(start<=last and not found):
		print
		middle=(start+last)//2
		if(myList[middle]==num_to_search):
			found=True
		else:
			if(num_to_search<myList[middle]):
				last=middle-1
			else:
				start=middle+1
	return found

a=[1,2,3,4,5]
print(binarySearch(a,4))



