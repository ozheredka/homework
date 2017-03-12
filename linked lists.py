class Node:
    def __init__(self, data, next=None, position = 0):
        self.data = data
        self.next = next
        self.position = position

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
        if self.head:
            return False
        return True

    def printList(self):
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next
        print()

    def push(self, data):
        node = Node(data, next=self.head)
        self.head = node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def delete(self, value):
        node = self.head
        next_node = node.next
        del (node)
        self.head = next_node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def reverse(head):
        new_head = None
        while head:
            temp = head
            head = temp.next
            temp.next = new_head
            new_head = temp
        return new_head

    def insert(self, item, position):
        if position == 0:
            self.push(data)
        else:
            temp = Node(item, position)
            current = self.head
            previous = None
            while current.position != position:
                previous = current
                current = current.next
            previous.next = temp
            temp.next = current
            temp.back = previous
            current.back = temp
            current = self.head



n3 = Node(3)
n2 = Node(2, next=n3)
n1 = Node(1, next=n2)


l = LinkedList(head=n1)
for i in [1,2,3,4,5,4,5,6,6,6,6,1,1,54,3]:
    l.append(i)
l.printList()
