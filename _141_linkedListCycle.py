from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1) #The "head"
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1  # Creates a cycle (pos=1 if you look at the leetcode)

class HashSetSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        node = head
        while node and node.next:
            if node in visitedNodes:
                return True
            else:
                visitedNodes.add(node)
            node = node.next
        return False
    

hashSol = HashSetSolution()
print(hashSol.hasCycle(node1))

class PointerSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        #fp: fast pointer, sP: slow pointer
        fp = head.next
        sp = head

        while fp and sp:
            if fp == sp: #Found loop
                return True
            
            if not fp.next:
                return False
            
            fp = fp.next.next
            sp = sp.next
        
        return False

pointSol = PointerSolution()
print(pointSol.hasCycle(node1))