n =int(input())
for i in range(1,n+1):
    if i == n:
        print(" " * (n-i)+ "#" * i) 
    else:
        print(" " * (n-i) + "*" * i) 