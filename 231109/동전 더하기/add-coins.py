#입력
n,k=map(int,input().split())
money=[int(input()) for _ in range(n)]

#큰동전부터 다시배열
money=sorted(money,reverse=True)
answer=0
for m in money:
    answer+=k//m
    if k//m>0: #굳이 if문 없어도 되네용
        k=k%m
print(answer)