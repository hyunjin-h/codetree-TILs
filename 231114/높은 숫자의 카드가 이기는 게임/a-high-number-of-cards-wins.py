n=int(input())
acards=[a for a in range(1,2*n+1)]
bcards=[]
for _ in range(n):
    card=int(input())
    acards.remove(card)
    bcards.append(card)

acards.sort()
bcards.sort()
cnt=0
check_B = 0

for i in range(n):
    if check_B == i:
        if acards[i] > bcards[i]:
            cnt += 1
            check_B = i+1
        else:
            check_B = i

    else:
        if acards[i] > bcards[check_B]:
            cnt += 1
            check_B += 1

print(cnt)