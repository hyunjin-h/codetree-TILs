n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
ans=0
def count(x,y):
    cnt=0
    for nx in range(x,x+3):
        for ny in range(y,y+3):
            cnt+=arr[nx][ny]

    return cnt

for row in range((n-3)+1):
    for col in range(n-3+1):
        ans=max(ans,count(row,col))

print(ans)