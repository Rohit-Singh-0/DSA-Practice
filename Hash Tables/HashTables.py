class HashMap:
    #Creating the cosntructor for the data map with default length of 7 with values as None
    def __init__(self, length = 7):
        self.data_map = [None]*length

    #Creating the hash function to create a hash for the index for the data map with the given key
    def __hash(self, key):
        my_hash = 0+ord(key[0])*23 % len(self.data_map)
        return my_hash

    #Creating the print table method to print the whole hash table
    def print_table(self):
        for key,value in enumerate(self.data_map):
            print(key,":",value)

    #Creating the set item method to set the value of the item at the given key
    def set_item(self,key, value):
        #Get the index for key
        index = self.__hash(key)
        #if it is None at the index then create an empty list
        if self.data_map[index] == None:
            self.data_map[index] = []
        #If its not empty then append the key value pair at the index
        self.data_map[index].append([key,value])

    #Created the get item method to get an item from the hash table according to the given key
    def get_item(self, key):
        #Get the index for the given key by using the hash method
        index = self.__hash(key)
        #If the data map is not empty at the index then loop through the elements at the index untill the key is found if found return
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        #if the data map is empty at the index return None
        return None

hT = HashMap()
hT.print_table()
print(" ")
hT.set_item("name", "your name")
hT.set_item("age", 22)
hT.set_item("occupation", "student")
hT.set_item("Skill Level", 1)
hT.print_table()
print(" ")
print("age:", hT.get_item("age"))