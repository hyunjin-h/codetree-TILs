n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
ans=0

#1번째케이스
for i in range(n-1):
    for j in range(m-1):
        cur_min=min(arr[i][j],arr[i+1][j],arr[i][j+1],arr[i+1][j+1])
        cur_sum=arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]
        cur_sum=cur_sum-cur_min
        ans=max(ans,cur_sum)

#2번째케이스
#가로탐색
for i in range(n):
    for j in range(m-2):
        cur_sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]
        ans=max(ans,cur_sum)
        
#세로탐색
for i in range(m):
    for j in range(n-2):
        cur_sum=arr[j][i]+arr[j+1][i]+arr[j+2][i]
        ans=max(ans,cur_sum)

print(ans)