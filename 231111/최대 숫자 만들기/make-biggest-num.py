n=int(input())
nums=[input() for _ in range(n)]

nums.sort()
for i in range(len(nums)-1):
    if nums[i][0]==nums[i+1][0]:
        x=nums[i]+nums[i+1]
        y=nums[i+1]+nums[i]
        if int(x)>int(y):
            nums[i],nums[i+1]=nums[i+1],nums[i]
nums.reverse()
print(''.join(nums))