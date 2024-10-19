n = int(input())
m = n+1
for i in range(m):
    if i == 0 :
        print("_" * (m-i) ) 
    else:
        print("|" * 1 + " " * (n-i) + "/" * 1)