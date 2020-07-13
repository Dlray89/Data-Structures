class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addtofront(self, data):
        # create a instance of the Node class and assign data to Node(data)
        new_node = Node(data)

        # setting the next value of the node to nene
        new_node.next = self.head
        # assigning head to the new node
        self.head = new_node

    def addafter(self, node, data):
        # if node is empty
        if node is None:
            print('the given previous node must in linkedlist')
            return
        # create a new instance of node
        new_node = Node(data)
        # setting next value to none
        new_node.next = node.next
        # setting the next value to next node if there of more than 1 node
        node.next = new_node

    def addtoend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next


    def removeNode(self, position):

        if self.head is None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        for i in range(position - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next


    # print the linked list
    def printList(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.value) + '', end='-->')
            temp_node = temp_node.next



if __name__ == '__main__':

    llist = LinkedList()
    llist.addtoend(1)
    llist.addtofront(2)
    llist.addtofront(3)
    llist.addtoend(4)
    llist.addafter(llist.head.next, 5)

    print('Linked list')
    llist.printList()

    print('\nafter del an elment')
    llist.removeNode(3)
    llist.printList()
