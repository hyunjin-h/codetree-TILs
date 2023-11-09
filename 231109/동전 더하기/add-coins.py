n,k=map(int,input().split())
money=[int(input()) for _ in range(n)]
money=sorted(money,reverse=True)
answer=0
for m in money:
    answer+=k//m
    if k//m>0:
        k=k%m
print(answer)