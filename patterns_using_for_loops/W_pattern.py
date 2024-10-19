n = int(input())
for i in range (n):
    if i == 0:
        row = " " * i + "* " * (n-i) + " "*(2*(i-1)) + "* "*((n-i-1))
        print(row)
        
    else:
        row = " " * i + "* " * (n-i) + " "*(2*(i-1)) + "* "*((n-i-1)+1)
        print(row)
        