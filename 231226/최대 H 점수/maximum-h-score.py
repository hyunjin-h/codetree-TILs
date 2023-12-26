n, l = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
print(arr)
h=0
for i, a in enumerate(arr):
    if len(arr)-i>=a:
        h=max(h,a)

print(h)