n = int(input())
r500 = int(n/500)
rem500 = n%500
r50 = int(rem500/50)
rem50 = rem500%50
r10 = int(rem50/10)
rem10 = rem50%10
print(f"500: {r500} 50: {r50} 10: {r10} 1: {rem10}")