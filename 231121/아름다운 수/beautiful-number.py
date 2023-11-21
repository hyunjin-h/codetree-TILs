n=int(input())
answer=[]
result=0
def check():
    global result
    pre=answer[0]
    cnt=1
    if n==1:
        result=1
        return 0
    for i in range(1,n):
        if pre==answer[i]:
            cnt+=1
        else:
            cnt=1
            if i==n-1:
                return 0         
        if cnt%pre==0:
            cnt=0
        else:
            return 0
        pre=answer[i]
    result+=1



def make(curr_num):
    if curr_num==n:
        check()
        return 0
    for i in range(1,5):
        answer.append(i)
        make(curr_num+1)
        answer.pop()


    
    
    
make(0)
print(result)