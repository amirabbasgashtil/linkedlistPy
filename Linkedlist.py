# Linked List in Python by Amirabbas Gashtil

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def print(self):

        #linkedList is empty
        if self.head is None:
            print('linkedList is empty')
            return
        else:
            iterator = self.head
            while iterator:
                print(iterator.data, ' ')
                iterator = iterator.next

    def  linkedList_length(self):
        if self.head is None:
            print('linkedList length is 0')
            return
        else:
            iterator = self.head
            counter = 0
            while iterator:
                counter += 1
                iterator = iterator.next
            return counter

    def add_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def add_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.add_at_begining(data)
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            iterator.next = node

    def insert_at(self, index, data):
        if index < 0 or index >= self.linkedList_length():
            print('invalid index')

        else:
            counter = 0
            iterator = self.head

            while counter != index - 1:
                iterator = iterator.next
                conter += 1

            node = Node(data, iterator.next)

            node.next = iterator.next
            iterator.next = node

    # delete the last value
    def pop(self):
        if self.head is None:
            print('linkedList is empty')

        else:
            iterator = self.head
            counter = 0
            while iterator:
                if  counter == self.linkedList_length() - 2:
                    iterator.next = iterator.next.next
                    break
                iterator = iterator.next
                counter += 1

if __name__ == '__main__':
    list = linkedList()

    