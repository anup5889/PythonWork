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

