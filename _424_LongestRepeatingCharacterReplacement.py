from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    l, r = 0, 0
    mostFreqLetter=s[0]
    output=0
    for i, c in enumerate(s):
        r += 1
        letterData = max(Counter(s[l:r]).items(), key=lambda x: x[1])
        mostFreqLetter = letterData[0]
        numOfOccurrences = letterData[1]
        while (r - l) - numOfOccurrences > k:
            l += 1
        output = max(output, (r-l))
    return output

print(characterReplacement("AABABBA", 1))