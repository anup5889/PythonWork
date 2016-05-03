"""

n th fibonacci number
1 1 2 3 5

"""


def fib(n):

	count=1
	prevEle=1
	currentEle=1
	while True:
		NextEle=prevEle+currentEle
		count+=1
		if count==n:
			return NextEle
		prevEle=currentEle
		currentEle=NextEle

print fib(4)


def fibRecurssive(n):

	if n==0 or n==1:
		return 1
	return fibRecurssive(n-1)+fibRecurssive(n-2)

print fibRecurssive(4)

class fibUsingMemoize:
	def __init__(self):
		self.memo={}

	def fibUsingMemo(self,n):

		if n<0:
			raise Exception("The input should be positive integer")
		elif n in [0,1]:
		   return 1

		if n in self.memo:
			return self.memo[n]
		
		result=self.fibUsingMemo(n-1)+self.fibUsingMemo(n-2)
		self.memo[n]=result

		return result

fibIns=fibUsingMemoize()
print fibIns.fibUsingMemo(4)









