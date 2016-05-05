
class TempTracker:
    def __init__(self):
        self.min_temp=None
        self.max_temp=None
        self.sum_temp=0
        self.count=0
    def insert(self,temp):
        self.count+=1
        self.sum_temp+=temp
        if (self.max_temp is None) or (temp>self.max_temp):
            self.max_temp=temp
        if (self.min_temp is None) or (temp<self.min_temp):
            self.min_temp=temp

    def get_max(self):
        return self.max_temp
    def get_min(self):
        return self.min_temp
    def get_mean(self):
        return self.sum_temp/float(self.count)
    def get_mode(self):
        return self.tempList[len(self.tempList)/2]
tmpSystem=TempTracker()

tmpSystem.insert(109)
tmpSystem.insert
print tmpSystem.get_max()
print tmpSystem.get_min()
print tmpSystem.get_mean()
#print tmpSystem.get_mode()