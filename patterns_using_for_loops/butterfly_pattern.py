n = int(input())
for i in range(2*n-1):
    if i < n:
        stars = "* " * (i+1) + "  " * (2 * (n-(i+1))) + "* " * (i+1) 
        print(stars) 
    else:
        row = "* " * (2*n - (i+1) ) + "  " * (2 * (i-n+1) ) + "* " * (2*n - (i+1) )
        print(row)