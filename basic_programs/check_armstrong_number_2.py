n = int(input())
s = str(n)
sum = 0
length = len(s)
for i in range(length):
    sum = sum + (int(s[i])) ** length
if(sum == n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")