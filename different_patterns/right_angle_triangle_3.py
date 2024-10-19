n = int(input())
count  = 0
while count < n:
    count = count + 1
    if count == n:
        print("+ " * count)
    else:
        print("* " * count)