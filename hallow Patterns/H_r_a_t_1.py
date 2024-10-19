n = int(input())
for i in range(n):
    if i == 0 or i == n-1 or i == 1:
        print("* " * (i+1))
    else:
        print("* " * 1 + "  " * (i-1) + "* " * 1)