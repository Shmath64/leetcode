from typing import *
def threeSum(nums: List[int]) -> List[List[int]]:
    triplets = []
    #i != j != k and nums[i] + nums[j] + nums[k] == 0
    #NO duplicates
    #Going to sort the list, then just do two pointers

    #Final testcase takes too long to sort

    nums.sort() #O(n log n)

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        left, right = i + 1, len(nums) - 1

        #Now, two pointers:
        while left < right:
            theSum = a + nums[right] + nums[left]

            if theSum > 0:
                right -= 1
            elif theSum < 0:
                left += 1
            else:
                triplets.append([a, nums[left], nums[right]])
                left += 1
                #Needed for when there are duplicate nums
                while nums[left] == nums[left-1] and left < right:
                    left += 1
        
    return triplets    
        
threeSum([-2,0,1,1,2])