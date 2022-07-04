class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        else:
            prob_range = self.get_prob_range(h)
            for prob_index in prob_range:
                element = self.arr[prob_index]
                if element is None:
                    return
                if element[0] == key:
                    return element[1]

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception('HashMap is Full')

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)


t = HashTable()
t['march 9'] = 20
t['march 17'] = 52
t['march 6'] = 96
# print(t['march 17'])
# del t['march 9']
# print(t.arr)
# print(t.get_prob_range(9))
print(t.get_hash('march 6'))