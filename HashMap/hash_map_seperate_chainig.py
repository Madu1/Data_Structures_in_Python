# Implement the hash table based off the separate chaining concept
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    # get the hash value
    def get_hash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                # self.arr[h][index] = None
                del self.arr[h][index]


t = HashTable()
# t['march 6'] = 12
# t['march 17'] = 25
t['march 17']
