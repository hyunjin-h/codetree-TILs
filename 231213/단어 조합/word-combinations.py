n,m=map(int,input().split())
words=[input() for _ in range(n)]

chance=m-len(''.join(words))-n+1

def push_(chance):
    if chance==0:
        return 

    for i in range(1,n):
        if words[i]>'_':
            words[i]=list(words[i])
            words[i].insert(0,'_')
            words[i]=''.join(words[i])
            chance-=1
        if chance==0:
            return
    for i in range(n-1,0,-1):
        words[i]=list(words[i])
        words[i].insert(0,'_')
        words[i]=''.join(words[i])
        chance-=1
            
        if chance==0:
            return
    if chance>0:
        push_(chance)
push_(chance)

print('_'.join(words))