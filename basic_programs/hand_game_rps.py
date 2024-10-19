a = input()
b = input()
if a == "Rock" :
    if b == "Scissors":
        print("Abhinav Wins")
    elif b == "Paper" :
        print("Anjali Wins")
    else:
        print("Tie")
elif a == "Paper" :
    if b == "Scissors":
        print("Anjali Wins")
    elif b == "Paper" :
        print("Tie")
    else:
        print("Abhinav Wins")   
else  :
    if b == "Scissors":
        print("Tie")
    elif b == "Paper" :
        print("Abhinav Wins")
    else:
        print("Anjali Wins")   