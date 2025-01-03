from collections import defaultdict

def groupAnagrams(strs):
    ans = defaultdict(list)

    for word in strs:
        ans["".join(sorted(word))].append(word)

    print(ans)
    return ans.values()




def groupAnagrams2(strs):
    #Without using defaultDict
    ans = {}

    for word in strs:
        key = "".join(sorted(word))
        if key in ans.keys():
            ans[key].append(word)
        else:
            ans[key] = [word]
    
    return list(ans.values())


print(groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))