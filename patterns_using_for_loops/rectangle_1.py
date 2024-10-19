m =int(input())
n = int(input())
for i in range(m):
    if i == 0 or i== m-1 :
        print("* " * n)
    else:
        print("* " * 1 + "0 " * (n-2) + "* " * 1)