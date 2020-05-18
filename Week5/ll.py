class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linkedlist:
    def __init__(self,lst=[]):
        self.head=None
        for data in lst:
            node=Node(data)
            if not self.head:
                self.head=node
                self.tail=node
            else:
                self.tail.next=node
                self.tail=self.tail.next
        self.length=len(lst)

    def display(self):
        curr_node=self.head
        while curr_node is not None:
            print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
            curr_node=curr_node.next
        else:
            print('\033[44m',"None",'\033[0m')
            print()


def head_ll(data=[]):
    head=None
    for x in data:
        node=Node(x)
        node.next= head
        head=node
    return  head

def display_head(head):
    curr_node=head
    while curr_node is not None:
        print('\033[46m',curr_node.data,'\033[41m',end=" --\033[0m-->")
        curr_node=curr_node.next
    else:
        print('\033[44m',"None",'\033[0m')
        print()


ll=linkedlist([5,4,5,6,1,5,2,6])
ll.display()
display_head( head_ll([5,4,5,6,1,5,2,6][::-1]))
