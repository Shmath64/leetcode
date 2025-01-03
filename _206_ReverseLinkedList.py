from typing import Optional

"""
This script provides a couple methods for reversing singly linked lists
as well as a test and a function to display the lists
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Initiate 5 nodes with values 1-5
node1 = ListNode(1) #Head
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def reverseListIter(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a singly linked list iteratively
    """
    nodes = []
    currentNode = head

    while currentNode:
        nodes.append(currentNode)
        currentNode = currentNode.next
    
    for i in range(len(nodes)-1, 0, -1):
        if i > 0:
            nodes[i].next = nodes[i-1]
    
    nodes[0].next = None

    return head

def reverseListRec(head: Optional[ListNode], prevNode: Optional[ListNode] = None) -> Optional[ListNode]:
    """
    Reverses a singly linked list recursively
    """
    if head.next:
        reverseListRec(head=head.next, prevNode=head)
    head.next = prevNode #note that prevNode will be null at the head

def displayNodes(head: ListNode) -> None:
    currentNode = head
    while currentNode:
        print(f"{currentNode.val}->", end="")
        currentNode = currentNode.next
    print("None")

print("Nodes before reversal:")
displayNodes(node1) #Node 1 is the original head
print("Nodes after iterative reversal:")
reverseListIter(node1) #Reverse beginning at head
displayNodes(node5) #Node 5 is the new head
print("Nodes after recursive reversal (setting back to original order):")
reverseListRec(node5)
displayNodes(node1)
#This outputs:
"""
Nodes before reversal:
1->2->3->4->5->None
Nodes after iterative reversal:
5->4->3->2->1->None
Nodes after recursive reversal (setting back to original):
1->2->3->4->5->None
"""