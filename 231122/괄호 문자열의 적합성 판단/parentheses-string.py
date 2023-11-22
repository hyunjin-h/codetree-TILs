string=input()
stack=[]
def answer():
    for i in range(len(string)):
        if string[i]==')':
            if not stack or stack.pop()!='(':
                print('No')
                return 0
        if string[i]=='(':
            stack.append(string[i])

    if not stack:
        print('Yes')
        return 0
    else:
        print('No')
        return 0
answer()