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
        #The other normal case when the new node gets added at the end.
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1


#Creating the print list method to print all the values of the Linked List
    def print_list(self):
        #Creating a pointer for self.head named temp
        temp = self.head
        #when there are elements in the linked list print all the values with the while loop
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Creating the pop method to remove the last element from the Linked List
    def pop(self):
        if self.length == 0:
            self.head = None
            self.tail = None
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #now point the head to the new node/ assign the new node as the head of the linked list
            self.head= new_node
            #Now the head/new_node's next attribute is pointing to None according to the Node constructor so we have to join this node to the linked List so we will point the next attribute to temp(previous head)
            self.head.next = temp
        self.length += 1
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
        if self.length==0:
            self.head = None
            self.tail = None
        self.length-=1
        #return the popped node
        return temp.value

    #Creating the get method for the linked list
    def get(self, index):
        #if index out of bounds return none
        if index<1 or index>self.length:
            return None
        #if index is 1 then return the head
        elif index == 0:
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

    #Creating the insert method
    def insert(self, index, value):
        # if the index is out of bounds then return false
        if index < 0 or index > self.length:
            return False
        #if index is 1 then we can use the prepend method
        if index == 0:
            self.prepend(value)
            return True
        #if index equals to the lenght of the list then we can just use the append method
        elif index == self.length:
            self.append(value)
            return True
        # create a new node which we need to add
        new_node = Node(value)
        #get a pointer at the previous index of the given index
        prev = self.get(index-1)
        # now point the new node to the succ node
        new_node.next = prev.next
        #point the prev node to the new node
        prev.next = new_node
        #increase the length as we have added a node to the list
        self.length+=1
        return True

    #creating the remove method
    def remove(self,index):
        #if index is 1 we can use the pop first method
        if index == 0:
            return self.pop_first()
            #if index is the length of the list just use the pop method
        elif index == self.length:
            return self.pop()
        #if index out of bounds return False
        elif index<0 or index> self.length:
            return None
        #get pointers for the index, previous to the index and the succeding node to the index
        temp = self.get(index)
        prev = self.get(index-1)
        succ = self.get(index+1)
        #point the next pointer of prev to succ
        prev.next = succ
        #point the next pointer of temp to None so that it gets isolated/disconnected from the linked list
        temp.next = None
        #decrease the length of the linked list by 1
        self.length -=1
        #return the removed node
        return temp

    #Creating a reverse function to reverse the whole linked list
    def reverse(self):
        # Set up pointers for reversing
        temp = self.head
        self.head, self.tail = self.tail, self.head  # Swap head and tail
        prev = None

        # Loop to reverse each node's pointer
        while temp is not None:
            # Save the next node
            next_node = temp.next
            # Reverse the direction of the current node's next pointer
            temp.next = prev
            # Move prev and temp one step forward
            prev = temp
            temp = next_node
        return self.head


#initialising the linked list object with head 10
ll = LinkedList(0)
#append 1,2,3,4 in the linked list
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
#printing the linked list to check if the append method is working or not
print("Printed Linked List should be 0 1 2 3 4")
ll.print_list()
print("Current length of the Linked List is", ll.length)

print("--------------")

print("Now we will be popping the last element(i.e 4) of the Linked List with pop method.")
ll.pop()
print("Printed Linked List should be: 0 1 2 3")
ll.print_list()
print("Current length of the Linked List is", ll.length)

print("--------------")

print("Now we will be testing the prepend method and prepending 4 in the linked list.")
ll.prepend(4)
print("Printed Linked List should be: 4 0 1 2 3")
ll.print_list()
print("Current length of the Linked List is", ll.length)

print("--------------")
print("Now we will be testing the pop first method and it should pop 4 from the linked list.")
ll.pop_first()
print("Printed Linked List should be: 0 1 2 3")
ll.print_list()
print("Current length of the Linked List is", ll.length)

print("--------------")
print("Now we will be testing the get method by fetching the node at index 2.")
fetched_node = ll.get(2)
print("The printed value of the fetched node should be 2")
print(fetched_node.value)
print("Current length of the Linked List is", ll.length)

print("--------------")
print("Now we will be testing the set method by changing the index 1 with value 5.")
ll.set(1,5)
print("The printed linked list should be: 0 5 2 3")
ll.print_list()
print("Current length of the Linked List is", ll.length)

print("--------------")
print("Now we will be testing the insert method by inserting value 6 at index 2.")
ll.insert(2,6)
print("The printed linked list should be: 0 5 6 2 3")
ll.print_list()
print("Current length of the Linked List is", ll.length)
print("--------------")
print("Now we will be testing the remove method by removing the index 3.")
ll.remove(3)
print("The printed linked list should be: 0 5 6 3")
ll.print_list()
print("Current length of the Linked List is", ll.length)

print("--------------")
print("Now we will be reversing the linked list.")
ll.reverse()
print("The printed linked list should be: 3 6 5 0")
ll.print_list()
print("Current length of the Linked List is", ll.length)