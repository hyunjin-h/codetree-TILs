n=int(input())
nums=list(map(int,input().split()))

arr=nums
answer=0
while len(arr)>1:
    arr.sort()
    pay=arr[0]+arr[1]
    answer+=pay
    arr=arr[2:]
    arr.append(pay)

print(answer)