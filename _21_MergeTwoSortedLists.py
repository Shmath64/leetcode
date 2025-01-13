from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating the first linked list [1, 2, 4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Creating the second linked list [1, 3, 4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive Approach

        
        if not list1:
            return list2
        if not list2:
            return list1
        #Base Case: This will return None if both are None, if one is None, the other is returned

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach

        if not list1:
            return list2
        if not list2:
            return list1
        
        #Initialize head:
        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        tail = head

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                #tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                #tail = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return head

        
        

#Not part of the question
def displayList(head: Optional[ListNode]) -> None:
    if head:
        print(f"{head.val} ", end="")
    if not head:
        print("")
        return
    displayList(head.next)

sol = Solution1() #Solution1 for recursive, Solution2 for iterative

displayList(sol.mergeTwoLists(list1, list2))
displayList(sol.mergeTwoLists(None, ListNode(0)))

