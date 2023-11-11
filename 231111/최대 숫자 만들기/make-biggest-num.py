from functools import cmp_to_key

n=int(input())
nums=[input() for _ in range(n)]

def compare(x, y):
    if x == y: return 0 # 같다면 상관 없다
    if x + y > y + x: return -1
    else: return 1

nums = sorted(nums, key=cmp_to_key(compare))
print(''.join(nums))