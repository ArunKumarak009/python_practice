n = int(input())
for i in range(n):
    if i == 0:
        print("* " * (n-i)) 
    else:
        print("+ " * (n-i))
