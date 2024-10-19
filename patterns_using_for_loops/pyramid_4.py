n = int(input())
for i in range(2*n-1):
    if i<n:
       spaces = "  " * (n-(i+1))
       plus = "+ " * i 
       has = "# " * 1 
       print(spaces + plus + has)
    else:   
       spaces_1 = "  " * ((i + 1-n)) 
       plus_1 = "+ " * (2*n - (i+2)) 
       has_1 = "# " * 1 
       print(spaces_1 + plus_1 + has_1)