string=input()
stack=[]
for i in range(len(string)):
    if string[i]==')':
        if not stack or stack.pop()!='(':
            print('No')
    if string[i]=='(':
        stack.append(string[i])

if not stack:
    print('Yes')
else:
    print('No')