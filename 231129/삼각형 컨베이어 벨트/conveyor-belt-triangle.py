n,t=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a3=list(map(int,input().split()))
belt=a1+a2+a3

for i in range(t):
    temp=belt[-1]
    for j in range(len(belt)-1,0,-1):
        belt[j]=belt[j-1]
    belt[0]=temp

for i in range(len(belt)):
    print(belt[i],end=' ')
    if i%3==n-1:
        print()