#입력
n=int(input())
arr=list(map(int,input().split()))

# max slice sum
def solution(A):
    max_ending = 0
    max_slice = A[0]
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

print(solution(arr))