#Creating the Node Constructor first
class Node:
    #Constructor Function for creating the Node object with the given value
    def __init__(self, value):
        #assigning the given value to the Node
        self.value = value
        #Assigning the next Node to None
        self.next = None

#Creating the LinkedList Constructor with all the LinkedList methods.
class LinkedList:
    #Coonstructor function for creating the LinkedList object
    def __init__(self, value):
        #Creating a new node with the passed value
        new_node = Node(value)
        #Since this is the constructor function the head and tail of the linked list is assigned to this new node
        self.head = new_node
        self.tail = new_node
        #Assigning the length attribute and giving it the value 1 as this is just created
        self.length = 1

    #Creating the append function to add a new node with a given value at the end of the Linked List
    def append(self, value):
        new_node = Node(value)
        #End Case when the head is None AKA the Linked List is Empty
        if not self.head:

            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        #The other normal case when the new node gets added at the end.
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1
            return True

    def print_list(self):
        temp = self.head
        if not temp:
            return None
        while temp:
            print(temp.value)
            temp = temp.next

LL = LinkedList(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.print_list()
