#Created the node class with next and value attributes
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

#Created the Queue class
class Queue:
    #Initialising the Queue object with first,last and length attributes
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    #method to print the whole queue
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    #Method to add a node in the queue
    def enqueue(self,value):
        #creating the node to add with the given value
        new_node = Node(value)
        #if the length of queue is 0 then the new node is the first and last of the queue
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        #else we add the new node in the end and update the last pointer
        else:
            self.last.next = new_node
            self.last = new_node
        #Increase the length of the queue by 1 after adding the node
        self.length += 1
        return True

    #Method to remove the first node from the queue as in queue FIFO(first in first out) pprinciple works
    def dequeue(self):
        #If the length of queue is 0 then there is nothing to remove so return none
        if self.length == 0:
            return None
        #Create a pointer for the first node
        temp = self.first
        #if the lenght of the queue is 1 then we can point both first and last pointer to none
        if self.length == 1:
            self.first = None
            self.last = None
        #else we have to point the first pointer to its next node and point the temp's next pointer to none
        else:
            self.first = self.first.next
            temp.next = None
        #Decrease the length of the queue by 1 as 1 node is removed
        self.length -= 1
        #return the removed node
        return temp

queue = Queue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print("Queue after enqueuing 0 1 2 3 4 5 6")
queue.print_queue()
queue.dequeue()
queue.dequeue()
print("Queue after Dequeuing 2 times:")
queue.print_queue()

