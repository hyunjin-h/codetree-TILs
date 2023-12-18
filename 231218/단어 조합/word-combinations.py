#10100sam님 코드참고
n, m = map(int, input().split())
total_length = 0
blank_length = n-1  # '_'가 들어갈 자리의 길이

words = []
for _ in range(n):
    word = input()
    total_length += len(word)
    words.append(word)

div = (m - total_length) // blank_length # '_'가 기본적으로 몇개 들어갈지 세팅해주기 위함
mod = (m - total_length) % blank_length # 남은 '_'

blanks = [div] * blank_length
# 최초 blank 처리
for i in range(1, n):
    word = words[i]
    ordinal = ord(word[0])
    if mod > 0 and ordinal > 90:    # 소문자라면
        blanks[i-1] += 1            # 앞에 '_'갯수 하나 추가!
        mod -= 1                    # 남은'_'갯수 업데이트

# 최종 blank 처리
j = len(blanks) - 1 # 뒤에서부터 하나씩 추가, 사전순으로 앞서는 단어를 만들기 위해
while mod != 0:
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