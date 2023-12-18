n, m = map(int, input().split())
total_length = 0
blank_length = n-1

words = []
for _ in range(n):
    word = input()
    total_length += len(word)
    words.append(word)

div = (m - total_length) // blank_length
mod = (m - total_length) % blank_length

blanks = [div] * blank_length
# 최초 blank 처리
for i in range(1, n):
    word = words[i]
    ordinal = ord(word[0])
    if mod > 0 and ordinal > 90:  # 대문자
        blanks[i-1] += 1
        mod -= 1

# 최종 blank 처리
j = len(blanks) - 1
while mod != 0:
    if blanks[j]<max(blanks):
        blanks[j] += 1
        mod -= 1
    j -= 1

res = ''
for i in range(n):
    res += words[i]

    if i == n-1:
        break
    
    res += '_' * blanks[i]

print(res)