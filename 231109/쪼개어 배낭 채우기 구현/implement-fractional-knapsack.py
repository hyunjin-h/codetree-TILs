#입력
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    w,v=map(int,input().split())
    arr.append([v/w,w,v])

#큰가치를 가진 보석 순 정렬
arr=sorted(arr, reverse=True)
bag=m
ans=0
for a in arr:
    if bag>=a[1]:
        ans+=a[0]*a[1]
        bag-=a[1]
    else:
        ans+=a[0]*bag
        break

print('{:.3f}'.format(ans))