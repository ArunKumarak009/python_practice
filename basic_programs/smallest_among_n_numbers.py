n = int(input())
temp = 0

for i in range(n):
    a = int(input())
    if(i == 0):
        temp = a 
    else:
        if(a < temp):
            temp = a
print(temp)