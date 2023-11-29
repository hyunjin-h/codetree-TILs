n,t=map(int,input().split())
belt1=list(map(int,input().split()))
belt2=list(map(int,input().split()))

belt=belt1+belt2
for i in range(t):
    temp=belt[-1]
    for j in range(len(belt)-1,0,-1):
        belt[j]=belt[j-1]
    belt[0]=temp
for i in range(n):
    print(belt[i],end=' ')
print()
for i in range(n,len(belt)):
    print(belt[i],end=' ')