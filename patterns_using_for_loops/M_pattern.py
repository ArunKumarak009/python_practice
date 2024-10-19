n = int(input())
for i in range(n):
    first_star = "* " * (i+1) 
    spaces = "  "* (2*(n-(i+1)))
    last_stars = "* " * (i+1)
    row = first_star + spaces + last_stars
    print(row)