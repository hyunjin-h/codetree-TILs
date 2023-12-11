n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
r,c=map(int,input().split())
r,c=r-1,c-1

def is_range(x,y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False
#폭발
def bomb(x,y):
    num=arr[x][y]
    arr[x][y]=0
    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(1,num):
        for j in range(4):
            nx=x+i*dx[j]
            ny=y+i*dy[j]
            if is_range(nx,ny):
                arr[nx][ny]=0
    

bomb(r,c)

#중력
for j in range(n):
    temp=[[0]*n for _ in range(n)]
    temp_row=n-1
    for i in range(n-1,-1,-1):
        if arr[i][j]!=0:
            temp[temp_row][j]=arr[i][j]
            temp_row-=1
        
    for row in range(n):
        arr[row][j]=temp[row][j]
        


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()