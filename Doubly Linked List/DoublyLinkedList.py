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

    def append(self, value):
        #creating a new node object with given value to add
        new_node = Node(value)
        #if list is empty then assign this node the head and tail pointers
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        #if not then join the new node at the end
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        #increase the length of list
        self.length += 1
        return True

    #Creating the print list method to print all the node values of the list
    def print_list(self):
        #pointer to the first node of the list
        temp = self.head
        #Loop the list and print the value of the pointer and increment it with every iteration.
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next


    #Creating the pop method to remove the last node from the list.
    def pop(self):
        #create a pointer to the previous node of tail which will be the new tail.
        temp = self.tail.prev
        #Create a pointer for the popped node to return later
        popped = self.tail
        #remove the last/tail node and assign the prevoius node as the new tail.
        self.tail.prev = None
        temp.next = None
        self.tail = temp
        #Decrease the length by 1 as we have removed 1 node from the list.
        self.length -= 1
        #return the popped node.
        return popped

    #Creating the prepend method to add a new node at the start of the DLL.
    def prepend(self,value):
        #create a new node with the given value
        new_node = Node(value)
        #if the list is empty then assign it the head and tail pointers
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        #if not then add it before the head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        #Increase the length of the list by 1
        self.length +=1
        return True

    #creating the pop first method to remove the first/head node of the list
    def pop_first(self):
        #create a pointer for the next node of the head
        temp = self.head.next
        #Create a pointer for the removed head node to return later
        popped = self.head
        #Isolate the head node
        self.head.next = None
        temp.prev = None
        #Point the head node to temp
        self.head = temp
        #decreas the length of the list by 1
        self.length -=1
        #return the popped node
        return popped

    #Creating the get method to easily access the node at a given index
    def get(self, index):
        #if index out of bounds return None
        if index<0 or index>=self.length:
            return None
        #if the index is 0 just return the first node
        elif index == 0:
            return self.head
        #if the index equals the length of the list then return the last/tail node
        elif index == self.length-1:
            return self.tail
        #create a pointer at head
        temp = self.head
        #loop throught the list and shift the pointer index number of times
        for _ in range(index):
            temp = temp.next
        #return the pointer
        return temp

    #creating the set method to change the value of the node at the given index with given value
    def set(self, index, value):
        #if index out of bounds return None
        if index<0 or index>=self.length:
            return None
        #if the index is 0 then change the value of head node
        elif index == 0:
            self.head.value = value
            return True
        #if the index equals the length of the list then update the value of tail node
        elif index == self.length-1:
            self.tail.value = value
            return True
        #if the index is in between get a pointer to the node at the index using the get method
        temp = self.get(index)
        #change the value of this node and return True
        temp.value = value
        return True

    #creating the insert method to insert a new node in the list
    def insert(self, index, value):
        # if index out of bounds return None
        if index < 0 or index >= self.length:
            return None
        # if the index is 0 then change the value of head node
        elif index == 0:
            return self.prepend(value)
        # if the index equals the length of the list then update the value of tail node
        elif index == self.length:
            return self.append(value)
        #if the index in betweeen
        else:
            new_node = Node(value)
            prev = self.get(index)
            temp = self.get(index+1)
            new_node.next = temp
            new_node.prev = prev
            prev.next = new_node
            temp.prev = new_node
        #increment the length of the list by 1
        self.length += 1
        return True


#Checking the Append method
print("Creating the Doubly Linked List with a value 1.")
DLL = DoublyLinkedList(1)
print("Appending 2,3,4 in the DLL. ")
DLL.append(2)
DLL.append(3)
DLL.append(4)
print("After appending the list should be: 1 2 3 4")
DLL.print_list()

print("-------------")

#checking the pop method
print("Popping the last Node of the DLl.")
popped = DLL.pop()
print("Popped element is:", popped.value)
print("The DLL after popping should be: 1 2 3")
DLL.print_list()

print("-------------")

#checking the prepend method
print("Prepending 0 to the DLL.")
DLL.prepend(0)
print("The List after prepending should be: 0 1 2 3")
DLL.print_list()

print("-------------")

#checking the pop first method
print("Popping the first/head node")
popped = DLL.pop_first()
print("The popped node is:", popped.value)
print("The list after popping the first node should be: 1 2 3")
DLL.print_list()

print("-------------")

#Checking the get method
print("The current list is:")
DLL.print_list()
print("1. Checking when the index out of bounds.(index= 244)")
print("Answer:",DLL.get(244))
print("2. Checking when index = 0.")
print("Answer:",DLL.get(0).value)
print("3. Checking when index is equal to the length of the list")
print("Answer:",DLL.get(2).value)
print("4. Checking when the index is in between.")
print("Answer:",DLL.get(1).value)

print("-------------")

#Checking the set method
print("The current list is:")
DLL.print_list()
print("1. Checking when the index out of bounds.(index= 244)")
print("Answer:",DLL.set(244, 69))
print("2. Checking when index = 0 and value 6")
DLL.set(0, 6)
print("The current list is:")
DLL.print_list()
print("3. Checking when index is equal to the length of the list and value 9.")
DLL.set(2, 9)
print("The current list is:")
DLL.print_list()
print("4. Checking when the index is 1 and value 7.")
DLL.set(1, 7)
print("The current list is:")
DLL.print_list()

print("-------------")

#Checking the insert method
print("The current list is:")
DLL.print_list()
print("1. Checking when the index out of bounds.(index= 244, value =69)")
print("Answer:",DLL.insert(244, 69))
print("2. Checking when index = 0 and value 5")
DLL.insert(0, 5)
print("The current list is:")
DLL.print_list()
print("3. Checking when index is equal to the length of the list and value 9.")
DLL.insert(2, 10)
print("The current list is:")
DLL.print_list()
print("4. Checking when the index is 1 and value 7.")
DLL.insert(1, 8)
print("The current list is:")
DLL.print_list()