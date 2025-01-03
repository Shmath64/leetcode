def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    charSet = set()
    maxSubString = 0
    
    for r, c in enumerate(s):
        if c not in charSet:
            maxSubString = max(maxSubString, r-l+1)
            charSet.add(c)
        else:
            l=r
            charSet.clear()
            charSet.add(c)

    return maxSubString


print(lengthOfLongestSubstring("dvdf"))