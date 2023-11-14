n=int(input())
acards=[a for a in range(1,2*n+1)]
bcards=[]
for _ in range(n):
    card=int(input())
    acards.remove(card)
    bcards.append(card)

acards.sort()
bcards.sort()
ans=0
for i in range(n):
    if acards[i]<bcards[i]:
        if i!=n-1:
            acards[i],acards[i+1]=acards[i+1],acards[i]
    
    if acards[i]>bcards[i]:
        ans+=1

print(ans)