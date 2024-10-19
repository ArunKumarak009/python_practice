n = int(input())
for i in range(n):
    if i== 0:
        print(" " * i + "+ " * (n-i)) 
    else:
        print(" " * i + "* " * (n-i))