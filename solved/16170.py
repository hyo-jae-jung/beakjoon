import datetime 

now = datetime.datetime.today()
print(now.year)
print(str(now.month).rjust(2,"0"))
print(str(now.day).rjust(2,"0"))
