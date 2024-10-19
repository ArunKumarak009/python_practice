d = input()
n = int(input())
if d == "Monday":
    day = 0
elif d == "Tuesday":
    day = 1    
elif d == "Wednesday":
    day = 2
elif d == "Thursday":
   day = 3
elif d == "Friday":
    day = 4
elif d == "Saturday":
    day = 5
else :
    day = 6 
t = day + n -1
t = t%7
if t == 0:
    print("Monday")
elif t==1:
    print("Tuesday")
elif t==2:
    print("Wednesday")
elif t==3:
    print("Thursday")
elif t==4:
    print("Friday")
elif t==5:
    print("Saturday")
else:
    print("Sunday")