def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    theSum = numbers[left] + numbers[right]

    while theSum != target:
        if theSum > target:
            right -= 1
        else:
            left += 1
        theSum = numbers[left] + numbers[right]

    return [left, right]


print(twoSum([2,7,11,15], 9))