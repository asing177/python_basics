class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeCycle(head):
    ptr1 = head
    ptr2 = head
    flag = False

    while ptr2 != None and ptr2.next != None:
        ptr1= ptr1.next
        ptr2 = ptr2.next.next
        if ptr1 == ptr2:
            flag = True
            break

    if flag:
        ptr1= head
        while ptr1.next != ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next


    ptr2.next = None

    return head



head = Node(2)
head.next = l1 = Node(8)
l1.next = l2 = Node(4)
l2.next = l3 = Node(3)
l3.next = l4 = Node(2)
l4.next = l5 = Node(1)
l4.next = l2


removeCycle(head)


while head != None:
    print(f'{head.data}->',end="")
    head = head.next;



