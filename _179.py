def largestNumber(nums) -> str:
    stringOfDigits = list(''.join(map(str, nums)))
    stringOfDigits.sort(reverse=True)
    stringOfDigits = ''.join(stringOfDigits)
    print(stringOfDigits)

print(largestNumber([10, 2, 100, 300]))