class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def check_merge(lst1, lst2):
    ptr1 = lst1
    ptr2 = lst2

    flag = False

    while ptr1!= None and ptr2 != None and \
          ptr2.next != None and ptr1.next !=None:

        ptr1 = ptr1.next
        ptr2 = ptr2.next

        if ptr1 == ptr2:
            flag = True
            break




def print_list(lst):
    while lst != None:
        if lst.next == None:
            print(lst.data)
        else:
            print(f'{lst.data}->', end="")

        lst = lst.next




head1 = Node('A')
head1.next = n2 = Node('B')
n2.next = n3 = Node('C')
n3.next = n4 = Node('D')
n4.next = n5 = Node('E')
n5.next = n6 = Node('F')



head2 = Node('P')
head2.next = n6 = Node('Q')
n6.next = n7 = Node('R')
n7.next = n8 = Node('S')
n8.next = n3

print_list(head1)
print_list(head2)
check_merge(head1, head2)




