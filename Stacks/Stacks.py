#Create the Node class to create node objects in the Stack class with value and next pointer.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Create a stack class to create stack objects later with initialising attribute top and height
class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.height = 1

    #method to print the whole stack
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    #method to push/add nodes at the top of the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height+=1

    #method to remove the top Node from the stack
    def pop(self):
        #endcase
        if self.height==0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp


#check the push and print stack methods
print("Stack after pushing 0 1 2 3 4 5 6")
stack = Stack(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.print_stack()
print("-----------------")
#check the pop method
print("Stack after popping 2 times.")
stack.pop()
stack.pop()
stack.print_stack()