class HashMap:
    def __init__(self, length = 7):
        self.data_map = [None]*length

    def __hash(self, key):
        my_hash = 0+ord(key[0])*23 % len(self.data_map)
        return my_hash

    def print_table(self):
        for key,value in enumerate(self.data_map):
            print(key,":",value)

    def set_item(self,key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
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