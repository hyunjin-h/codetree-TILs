n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

arr=sorted(arr)
cnt=0
cur_end=-1
for a,b in arr:
    if a>=cur_end:
        cur_end=b
        cnt+=1
    
print(cnt)