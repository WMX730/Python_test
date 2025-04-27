nums = [6, 5, 3, 1, 8, 7, 2, 4]
for j in range(len(nums)):
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            temp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = temp
    print(nums)
print(nums)