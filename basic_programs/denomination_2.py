n = int(input())
r2000 = int(n/2000)
rem2000 = n%2000
r500 = int(rem2000/500)
rem500 = rem2000%500
r200 = int(rem500/200)
rem200 = rem500%200
r50 = int(rem200/50)
rem50 = rem200%50
r20 = int(rem50/20)
rem20 = rem50%20
r5 = int(rem20/5)
rem5 = rem20%5
r2 = int(rem5/2)
rem2 = rem5%2
print(f"2000:{r2000} 500:{r500} 200:{r200} 50:{r50} 20:{r20} 5:{r5} 2:{r2} 1:{rem2}")