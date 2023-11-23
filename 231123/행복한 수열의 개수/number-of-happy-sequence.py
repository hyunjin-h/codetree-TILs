n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]
pre=-1
cnt=1
max_cnt=0
ans=0
for i in range(n):
    for ele in arr[i]:
        
        if pre==ele:
            cnt+=1
            max_cnt=max(max_cnt,cnt)
        else:
            cnt=1

        if max_cnt>=m:
            ans+=1
            continue

for i in range(n):
    arr[j][i]