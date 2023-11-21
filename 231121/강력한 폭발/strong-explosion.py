n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

case1_dx=[-2,-1,1,2]
case1_dy=[0,0,0,0]
case2_dx=[-1,0,1,0]
case2_dy=[0,1,0,-1]
case3_dx=[-1,-1,1,1]
case3_dy=[-1,1,-1,1]

def is_available(x,y):
    if x>=0 and x<n and y>=0 and y<n and arr[x][y]==0:
        return True
    return False

def bomb(x,y):
    
    

cnt=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            cnt+=1
            bomb(i,j)


answer=sum(arr)-cnt
print(answer)