n,m=map(int,input().split())
words=[input() for _ in range(n)]

new='_'.join(words)
chance=m-len(new)
new=list(new)
def push_(chance):
    if chance==0:
        return 
    l=len(new)
    for i in range(l-1,-1,-1):
        if new[i]=='_':
            new.insert(i,'_')
            chance-=1
        if chance==0:
            return
    push_(chance)        
push_(chance)
print(''.join(new))