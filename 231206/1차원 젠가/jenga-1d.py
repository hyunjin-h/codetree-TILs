n=int(input())
arr=[int(input()) for _ in range(n)]
s1,e1=map(int,input().split())
s2,e2=map(int,input().split())

temp=[]
for i in range(len(arr)):
    if i>=s1-1 and i<=e1-1:
        continue
    else:
        temp.append(arr[i])
arr=temp
temp=[]

for i in range(len(arr)):
    if i>=s2-1 and i<=e2-1:
        continue
    else:
        temp.append(arr[i])
arr=temp
print(len(arr))
for i in range(len(arr)):
    print(arr[i])