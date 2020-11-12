class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = False



def traverse_list(lst):
    print("Traversing First list")
    ptr = lst

    while ptr != None and ptr.next != None:
        ptr.flag = True
        ptr = ptr.next




def check_merge(lst2):
    print("Checking for Merge")
    ptr2 = lst2

    flag = False

    while ptr2!= None and ptr2.next !=None:
            if ptr2.next.flag == True:
                flag = True
                break

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
traverse_list(head1)
check_merge(head2)