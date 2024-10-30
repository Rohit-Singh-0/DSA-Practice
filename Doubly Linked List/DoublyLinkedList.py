#creating the Node class with value,next and prev attributes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        #creating a Node object with the given value and assigning it the head and tail pointers
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        #As this node gets added to the DLL its length becomes 1
        self.length = 1


