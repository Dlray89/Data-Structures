#list = ['a, b, c, d, r, w, r, ']

# print(list[0])

# for i in range(len(list)):
#    print(list[i])


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

if __name__ =='__main__':
    linkedList = LinkedList()

    linkedList.head = Node(1)
    second = Node(2)
    thrid = Node(3)

    linkedList.head.next = second
    second.next = thrid


    while linkedList.head != None:
        print(linkedList.head.data, end= '->')
        linkedList.head = linkedList.head.next