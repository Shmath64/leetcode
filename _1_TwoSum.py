def twoSum(nums, target: int) -> list[int]:
    for i, num in enumerate(nums):

        #These caused occasional issues
        """
        if num > target and target > 0:
            continue
        elif num < target and target < 0:
            continue
        """
        numsWithoutNum = nums[:i] + nums[i+1:]

        if (target - num) in numsWithoutNum:
            return [i, numsWithoutNum.index(target-num)+1]
        
print(twoSum([-18,12,3,0], -6))