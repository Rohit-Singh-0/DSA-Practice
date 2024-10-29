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
    #Constructor function for creating the LinkedList object
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

#Creating the print list method to print all the values of the Linked List
    def print_list(self):
        #Creating a pointer for self.head named temp
        temp = self.head
        #Case: when the Linked List is empty
        if not temp:
            return None
        #Case: when there are elements in the linked list print all the values with the while loop
        while temp:
            print(temp.value)
            temp = temp.next

#Creating the pop method to remove the last element from the Linked List
    def pop(self):
        #creating a pointer to the head
        temp = self.head
        #creating a pointer to the tail to return the value at the end
        val = self.tail
        #Looping through the Linked list to the element just before the tail and the range is from 1 to length-1 because the indexing was from 1
        for _ in range(1, self.length-1):
            #moving the temp pointer to the element just before the tail
            temp = temp.next
        #changing the tail pointer to same as temp
        self.tail = temp
        #removing the last node
        temp.next = None
        #Decreasing the length attribute by 1
        self.length -= 1
        #returning the last removed element
        return val.value

#creating a prepend method to add an element at the start of the linked list
    def prepend(self, value):
        #create a new node with the given value
        new_node = Node(value)
        #create a pointer to head
        temp = self.head
        #case1: if head is none / empty linked list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        #now point the head to the new node/ assign the new node as the head of the linked list
        self.head= new_node
        #Now the head/new_node's next attribute is pointing to None according to the Node constructor so we have to join this node to the linked List so we will point the next attribute to temp(previous head)
        self.head.next = temp
        return True

#creating the pop first method to delete the first/head element of the linked list
    def pop_first(self):
        #if the head is none or the linked list is empty then return none
        if not self.head:
            return None
        #Create a pointer for the head
        temp = self.head
        #shift the head to the next node
        self.head = self.head.next
        #remove the first element by pointing its next attribute to none
        temp.next = None
        #return the popped node
        return temp.value

    #Creating the get method for the linked list
    def get(self, index):
        #if index out of bounds return none
        if index<1 or index>self.length:
            return None
        #if index is 1 then return the head
        elif index == 1:
            return self.head
        #if index is equal to the length of linked list then return the tail
        elif index == self.length:
            return self.tail
        #else create a pointer to head
        temp = self.head
        #shift the pointer to the index we need
        for _ in range(index):
            temp = temp.next
        #return the node at the index
        return temp

    #Creating the set method for the linked list
    def set(self, index,value):
        #check if index is in the bounds if not then return none
        if index<0 or index>self.length:
            return None
        #if the linked list is empty then return none
        elif self.length == 0:
            return None
        #get hold of the node at the index by get method
        node_to_change = self.get(index)
        #change its value to the given value
        node_to_change.value = value
        return True


LL = LinkedList(1)
LL.append(2)
LL.append(3)
LL.append(4)
LL.print_list()
print(LL.pop())
LL.print_list()
node = LL.get(3)
print(node.value)