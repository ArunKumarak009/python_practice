n = int(input())
for i in range(2*n-1):
    if i < n:
          first = (str(i+1) + " ") * (i+1)
          print(first)
    else:
        second = (str(2*n - (i+1)) + " " ) * ( 2*n - (i+1))
        print(second)