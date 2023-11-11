n=int(input())
meets=[list(map(int,input().split())) for _ in range(n)]

meets.sort(key=lambda x: x[1])
cnt=0
ending=0
for meet in meets:
    if meet[0]>=ending:
        cnt+=1
        ending=meet[1]

print(cnt)