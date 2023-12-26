n, l = map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

h=0
hi=0
for i, a in enumerate(arr):
    if len(arr)-i>=a:
        h=max(h,a)
        hi=i

while l>0 and hi>=0:
    arr[hi]+=1
    if len(arr)-hi>=arr[hi]:
        h=arr[hi]
    hi-=1
    l-=1

print(h)