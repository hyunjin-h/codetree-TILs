n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dxs=[1,-1,0,0]
dys=[0,0,-1,1]
visited=[[0 for _ in range(n)] for _ in range(n)]
people_cnt=0
people_list=[]
def can_go(x,y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    return False
cnt=0

def dfs(x,y):
    global people_cnt
    for dx,dy in zip(dxs,dys):
        nx=x+dx
        ny=y+dy
        if can_go(nx,ny):
            if visited[nx][ny]==0 and arr[nx][ny]==1:
                visited[nx][ny]=visited[x][y]+1
                people_cnt+=1
                dfs(nx,ny)
        


for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and arr[i][j]==1:
            visited[i][j]=1
            people_cnt=1
            dfs(i,j)
            people_list.append(people_cnt)
people_list.sort()
print(len(people_list))
for i in people_list:
    print(i)