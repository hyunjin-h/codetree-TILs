n=int(input())

cnt=n//5
n-=cnt*5
while n>0 and n%2!=0:
    cnt-=1
    n+=5
    if cnt==0:
        cnt=-1
        
if cnt!=-1:
    cnt+=n//2

print(cnt)