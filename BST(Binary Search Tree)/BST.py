#constructor for Node object with value, left and right attributes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#BST class for creating BST objects
class BinarySearchTree:
    def __init__(self):
        #Setting root equals to None to create an empty tree first
        self.root = None
    #insert method to add a node in the BST
    def insert(self, value):
        #creating the new node
        new_node = Node(value)
        #if the tree is empty assign the root to the new node abd return True
        if not self.root:
            self.root = new_node
            return True
        #creating a pointer for the root node
        temp = self.root
        #A loop which will run untill the new node is inserted
        while True:
            #if the newnode's value equal to the value of a node's value in the tree then return False
            if new_node.value == temp.value:
                return False
            #if the new node's value is less than the pointers value then travers towards the left side of the tree
            if new_node.value < temp.value:
                #if the left pointer of temp is empty then add the new node
                if temp.left is None:
                    temp.left = new_node
                    return True
                #if the left pointer of temp is not empty then move the temp pointer to the left
                temp = temp.left
            # if the new node's value is greater than the pointers value then travers towards the right side of the tree
            else:
                # if the right pointer of temp is empty then add the new node
                if temp.right is None:
                    temp.right = new_node
                    return True
                # if the right pointer of temp is not empty then move the temp pointer to the right
                temp = temp.right

    #creating the contain method to check if the given value is in the tree
    def contains(self,value):
        #if the tree is empty return False
        if self.root is None:
            return False
        #Create a temp pointer for root
        temp = self.root
        #Run the loop untill temp becomes None/ or the leaf of the tree with no further nodes
        while temp is not None:
            #if the value of temp pointer equals to the given value return True
            if value == temp.value:
                return True
            #if the given value is less than the temp's value shift temp to left
            if value<temp.value:
                temp = temp.left
            # if the given value is greater than the temp's value shift temp to right
            else:
                temp = temp.right
        #return False if value not found in the tree
        return False

BST = BinarySearchTree()

print(BST.root)
BST.insert(5)
BST.insert(3)
BST.insert(2)
BST.insert(7)
BST.insert(4)
BST.insert(6)
BST.insert(8)
print(BST.root.value)
print(f"{BST.root.left.value} {BST.root.right.value}")
print(f"{BST.root.left.left.value} {BST.root.left.right.value} {BST.root.right.left.value} {BST.root.right.right.value}")

print("The BST contains 9", BST.contains(9))
print("The BST contains 7", BST.contains(7))
print("The BST contains 6", BST.contains(6))
print("The BST contains 10", BST.contains(10))
print("The BST contains 5", BST.contains(5))
print("The BST contains 79", BST.contains(79))