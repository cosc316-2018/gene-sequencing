class HashTable:
    # courtesy of Carter(tm)
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.deleted= '\0'

    def put(self,key,data):
        '''
            Add a key value pair to the hastable.
        '''
        if (len(self)/self.size) > (8/10):
            temp = self.size + 1
            self.slots.append(None)
            self.data.append(None)
            self.size += 1
        while not self.is_prime_number(self.size):
            temp = self.size + 1
            self.slots.append(None)
            self.data.append(None)
            self.size += 1

        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                   nextslot = self.rehash(nextslot,len(self.slots))
            if self.slots[nextslot] == None:
                self.slots[nextslot]=key
                self.data[nextslot]=data
            else:
                self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        '''
            The algorithm/method/formula used to hash a given key
        '''
        return key%size

    def rehash(self,oldhash,size):
        '''
            If a value already exists at a particular index, 
            the key is rehashed to get a new index.
        '''
        return (oldhash+1)%size

    def get(self, key):
        '''
            Retrieve a key-value pair from the hash table
        '''
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    # magic methods that allow us to use some of the
    # methods above with python-specific keywords
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        count = 0
        for value in self.slots:
            if value != None:
                count += 1
        return count

    def __contains__(self,key):
        return self.get(int(key)) != None

    def delete(self, key):
        '''
            Delete a key value pair to the hastable.
        '''
        start_slot = self.hashfunction(key,len(self.slots))
        pos = start_slot
        current = self.slots[pos]
        while current != None:
            if current == key:
                self.slots[pos] = self.deleted
                self.data[pos] = self.deleted
                return None
            else:
                pos = self.rehash(pos, len(self.slots))
                current = self.slots[pos]
                if pos == start_slot:
                    return None

    def is_prime_number(self, x):
        '''
            Checks whether a given number is a prime number. This is
            used in the quadratic probing algorith for the hash table.
        '''
        if x >= 2:
            for y in range(2,x):
                if not ( x % y ):
                    return False
        else:
            return False
        return True
