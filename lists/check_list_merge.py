class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def check_merge(lst1, lst2):
    ptr1 = lst1
    ptr2 = lst2

    flag = False

    while ptr2!= None and ptr2.next !=None:
        ptr1 = lst1

        while ptr1!=None and ptr1.next != None:
            if ptr2.data == ptr1.data:
                flag = True
                break
            ptr1 = ptr1.next

        ptr2 = ptr2.next

    if flag:
        print("Lists are merging")




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
head2.next = n7 = Node('Q')
n7.next = n8 = Node('R')
n8.next = n9 = Node('S')
n9.next = n3

print_list(head1)
print_list(head2)
check_merge(head1, head2)




