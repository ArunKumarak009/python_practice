n = int(input())
n_string = str(n)
first = int(n_string[0])
second = int(n_string[1])
third = int(n_string[2])
first = first **3
second = second**3
third = third**3
if(first+second+third == n):
    print(True)
else:
    print(False)