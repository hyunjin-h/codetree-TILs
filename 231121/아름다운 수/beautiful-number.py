n = int(input())
ans = 0
num = []

def isBeautifulNum(num):
    i = 0
    while i < n:
        for j in range(i, i + num[i]):
            if j >= n or num[j] != num[i]:
                return False
        i += num[i]
    return True

def makeNum(cur):
    global num
    global ans

    if cur > n:
        if isBeautifulNum(num):
            ans += 1
        return
    
    for i in range(1, 5):
        num.append(i)
        makeNum(cur + 1)
        num.pop()

makeNum(1)
print(ans)