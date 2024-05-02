'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverseLinkedList(head):
    # write your code here
    current = head
    prev, nextnode= None, None
    while current:
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
    return prev