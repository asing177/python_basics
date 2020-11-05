class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isCycle(node):
    ptr1 = node
    ptr2 = node

    while ptr2 != None and ptr2.next != None:
        ptr1= ptr1.next
        ptr2 = ptr2.next.next

        if ptr1 == ptr2:
            return True

    return False


head = Node(2)
head.next = l1 = Node(8)
l1.next = l2 = Node(4)
l2.next = l3 = Node(3)
l3.next = l4 = Node(2)
l4.next = l5 = Node(1)
l4.next = l2

print(isCycle(head))