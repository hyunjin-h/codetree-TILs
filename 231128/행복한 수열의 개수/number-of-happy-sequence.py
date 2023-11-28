n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]
pre=-1
cnt=1
max_cnt=0
ans=0
if m==1:
    max_cnt=1
for i in range(n):
    pre=-1
    max_cnt=0
    if m==1:
        max_cnt=1
    for j in range(n):
        
        if pre==arr[i][j]:
            cnt+=1
            max_cnt=max(max_cnt,cnt)
        else:
            cnt=1
            pre=arr[i][j]

        if j==n-1 and max_cnt>=m:

            ans+=1
            max_cnt=0
            if m==1:
                max_cnt=1
            pre=-1
pre=-1
max_cnt=0
cnt=1
if m==1:
    max_cnt=1
for i in range(n):
    pre=-1
    max_cnt=0
    if m==1:
        max_cnt=1
    for j in range(n):
        if pre==arr[j][i]:
            cnt+=1
            max_cnt=max(max_cnt,cnt)
        else:
            cnt=1
            pre=arr[j][i]
        if j==n-1 and max_cnt>=m:

            ans+=1
            max_cnt=0
            if m==1:
                max_cnt=1
            pre=-1
print(ans)