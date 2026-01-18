
class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  #start of the list

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print(None)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5



l1 = LinkedList()
l1.head = node1
l1.print_list()
