import heapq
n=int(input())
arr=list(map(int,input().split()))

heapq.heapify(arr)
answer=0
while len(arr)>1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    heapq.heappush(arr,x+y)
    answer += x+y


print(answer)