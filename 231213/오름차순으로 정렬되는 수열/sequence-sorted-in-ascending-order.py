n=int(input())
arr=[int(input()) for _ in range(n)]
cnt=0
answer=[]
def chain():
    global cnt
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            cnt+=1
            answer.append((arr[i-1],arr[i]))
            arr[i-1],arr[i]=arr[i],arr[i-1]
            break
        if i==n-1:
            return
    chain()
chain()
print(len(set(answer)))