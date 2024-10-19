s = input()
length = len(s)
result = ""
for i in range(length):
    result = result + s[length-1]
    length = length - 1 
print(result)  