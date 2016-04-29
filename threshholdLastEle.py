
"""
Find out a last ele of fibonacci series when \
 previous_ratio-current_ratio>=some_threshold
fibonacci series is 1, 1, 2, 3, 5...

for instance: current ele is 2
prevEle: 1
NextEle:3

previous_ratio:2/1=2
current_ratio: 3/2=1.5

"""

def threshholdLastEle(some_value):

	prevEle=1.0
	CurrentEle=1.0
	while True:
		NextEle=prevEle+CurrentEle
		#print NextEle
		current_ratio=CurrentEle/(NextEle)
		#print current_ratio
		previous_ratio=CurrentEle/(prevEle)
		#print previous_ratio
		#print previous_ratio-current_ratio
		if ((previous_ratio-current_ratio)>=some_value):
			print prevEle, CurrentEle, NextEle
			print previous_ratio
			print current_ratio
			print previous_ratio-current_ratio
			return NextEle
				
		prevEle=CurrentEle
		CurrentEle=NextEle

	return NextEle

print threshholdLastEle(0.5)


