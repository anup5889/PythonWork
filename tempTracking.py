
class TempTracker:
    def __init__(self):
        self.tempList=[]
    def insert(self,temp):
        if temp>=0 and temp<=110:
        	self.tempList.append(temp)
    def get_max(self):
        if len(self.tempList)>0:
        	return max(self.tempList)
        else: 
            raise Exception("Empty List of Temperature")
    def get_min(self):
        return min(self.tempList)
    def get_mean(self):
        return sum(self.tempList)/len(self.tempList)
    def get_mode(self):
        return self.tempList[len(self.tempList)/2]
tmpSystem=TempTracker()

tmpSystem.insert(109)
print tmpSystem.get_max()
print tmpSystem.get_min()
print tmpSystem.get_mean()
print tmpSystem.get_mode()