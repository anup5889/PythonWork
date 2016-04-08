myList=[5, 3, 6, 8, 9, 10]

myList.sort()
"""
[3, 5, 6, 8, 9, 10]
"""

def binarySearch(myList):
	start=0
	num_to_search=int(input("Enter the number you want to search"))
	length_of_list= len(myList)
	end=length_of_list
	while(start<=end):
		mid=(start+end)/2
		if(myList[mid]==num_to_search):
			return mid
		elif num_to_search>myList[mid]:
			start=mid+1
		else:
			end=mid-1




#binarySearch(myList)

"""
[2, 6, 13, 21, 36, 47, 63, 81, 97]

start will be start element
case 1: x==A[mid]
case 2: x>A[mid]==> we will increase the start
to start==mid+1
case 3: x<A[mid]==> we will decrease the end to
end =mid-1



"""

def linearSearch(myList):
	num_to_search=int(input("Enter the number you want to search"))	
	for index, value in enumerate(myList):
		if num_to_search==value:
			print "Num to search found at ", index exit()
            
            

        else:
            print "number not found"



linearSearch(myList)

""" Linear Search Algorithm takes O(n) time """

	







