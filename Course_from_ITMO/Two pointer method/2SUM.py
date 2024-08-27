# numsss = [2, 7, 11, 15]    # Output: [0,1]
# target = 9

# numsss = [3,2,4] # Output: [1,2]
# target = 6

numsss = [3,3] # Output: [0,1]
target = 6


nums = sorted(numsss)
i = 0
j = len(nums) - 1

while nums[i] + nums[j] != target:
    if nums[i] + nums[j] > target:
        j -= 1
    if nums[i] + nums[j] < target:
        i += 1



print([numsss.index(nums[i]), numsss.index(nums[j], i + 1)])
