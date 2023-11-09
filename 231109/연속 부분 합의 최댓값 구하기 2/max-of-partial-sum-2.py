#입력
n=int(input())
arr=list(map(int,input().split()))

#sum_a가 0보다 작아지면 다음원소부터 다시 구간 만들기
ans=0
sum_a=0
for a in arr:
    sum_a+=a
    ans=max(ans,sum_a)
    if sum_a<0:
        sum_a=0
print(ans)