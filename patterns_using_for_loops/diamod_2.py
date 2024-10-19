n = int(input())
for i in range(2*n-1):
    if i < n :
        spaces = " " * (n-(i+1)) + ( str(i+1) + " " ) * (i+1)
        print(spaces)
    else:
        
        row_two = " " * (i+1-n) + (str(2*n-(i+1)) + " ") * (2*n-(i+1))
        print(row_two)