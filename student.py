PET=('Physics', 'Chemistry','Maths')
data={}


n=int(input("Enter the number of students:"))

for i in range(n):
    marks=[]
    name=input("Enter the name of the student %d" %(i+1))
    for sub in PET: 
        marks.append(int(input("Enter the marks of sub %s" %(sub))))
    data[name]=marks

for x,y in data.items():
    total=sum(y)
    print("%s's marks are %d" %(x,total))
    if(total<120):
        print("%s is failed" %(x))
    else:
        print("%s is passed" %(x))