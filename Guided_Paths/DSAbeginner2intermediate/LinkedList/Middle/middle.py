'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    f  = head
    nodes = []
    while f:
        nodes.append(f)
        f = f.next
    return nodes[len(nodes)//2]
'''
f = head
s= head
while f and f.next:
    f = f.next.next
    s = s.next
return s
'''