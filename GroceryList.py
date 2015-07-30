def help():
    print " What do you want to buy today?"
    print " Press: H for help \n Press N to Enter new Item"
grocery_list=[]
help()

while True:
    item= input(">>")
    grocery_list.append(item)
    new_item=input("Do you want to enter new item").lower()
    if new_item=='n' or 'no':
        exit()
    
