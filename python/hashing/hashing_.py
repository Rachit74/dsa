

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.size = 256 # size of the table (list)
        self.slots = [None for i in range(self.size)]
        self.count = 0 # number of sloets that are filled
    

    def _hash(self, key):
        hash_value = 0
        mlt = 1
        for c in key:
            hash_value += mlt * ord(c)
            mlt += 1

        return hash_value % self.size
    
    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break

            h = (h+1) % self.size

        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

        return "Inserted"

    def get(self, key):
        h = self._hash(key)

        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            
            h = (h+1) % self.size

        return None
    

ht = HashTable()
print(ht.put('name', 'Rachit'))
print(ht.put('age', 5))
print(ht.get('name'))

