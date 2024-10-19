n = int(input())
for i in range(n):
    print("  " * i + "* " * ((2*(n-1) + 1)))
    n=n-1