from typing import List

def generateSolution(n: int) -> List[str]:
    output = []

    #Recursive DFS solution to find all leaf nodes of the graph:
    #https://assets.leetcode.com/users/images/dabefcea-2a30-4a0a-81c4-b2dafcf9dce0_1599242411.2652733.png
    def dfs(openP, closeP, s):
        if openP == closeP == n:
            output.append(s)
            return
        
        #Add open parentheses if we have less than n, 
        #Add closed parentheses if we need more (closed parentheses must match open parentheses but can NEVER be more)

        if openP < n:
            dfs(openP + 1, closeP, s + "(")
        
        if closeP < openP:
            dfs(openP, closeP + 1, s + ")")

    dfs(0,0,"")

    return output