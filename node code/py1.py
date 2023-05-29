class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self, position):
        if self.head == None:
            return None

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return self.head

        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return None
        if temp.next is None:
            return None

        next = temp.next.next
        temp.next = None
        temp.next = next
        return self.head

