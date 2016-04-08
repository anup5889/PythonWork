import datetime
Birthday=input("Enter your birthdate in mm/dd/YYYY")
print type(Birthday)
Birthdate=datetime.datetime.strptime(str(Birthday)	,'%m/%d/%Y').date()

print Birthdate

