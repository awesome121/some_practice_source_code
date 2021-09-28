class QuadraticHashTable():
    """Is a child class of OpenAddressHashTable.
    If a collision then uses a quadratic probing function to find a free slot
    """

    def __init__(self, slots=11):
        """
        Creates a new hashtable with a number of slots (default: 10).
        Remember we can't have a load factor greater than 1 for an open hash...
        """
        self._data = [None for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0

    def _next_free_slot(self, first_hash):
        """Keeps incrementing hash index until an empty slot is found.
        Then returns the index of that slot"""
        curr_index = first_hash
        try_number = 0
        tried = []
        #print self._data
        while self._data[curr_index] is not None:
            tried.append(curr_index)
            if try_number + 1 >= self.n_slots // 2:
                #print self._data
                print('Size = ' + str(self.n_slots))
                print('Number of items = ' + str(self.n_items))
                print("Failed to find an empty slot...")
                print('Try number = '+str(try_number))
                print('List of tried slots = '+str(tried))
                print('Current table = '+str(self._data))
                raise ValueError("Failed to find an empty slot!!!! "+
                                 "This can happen with quadratic probing "+
                                 "if the table is over half full")
            else:
                try_number += 1
                curr_index = (first_hash + try_number**2) % self.n_slots
                print(curr_index)
        return curr_index

    def store(self, item):
        """Stores an item in the hashtable."""
        if self.n_slots == self.n_items:
            #Argh - crash, who made the hashtable too small?
            print(self._data)
            print('Size = ' + str(self.n_slots))
            print('Slots used = ' + str(self.n_items))
            print("Hash table is full!!!! You eeediot")
            print("A good Hasher would have resized the hash table by now!")
            raise ValueError("Hash table is full!!!!")
        # **************************************************
        # ---start student section---
        index = self._hash(item)
        if self._data[index] is not None:
            index = self._next_free_slot(index)
        self._data[index] = item
        
        # ===end student section===
        self.n_items += 1

    def _hash(self, item):
        """Computes the hash of an item."""
        return nice_hash(item) % self.n_slots

    def __contains__(self, item):
        """
        Checks to see if an item is stored within the hashtable.
        Returns True if it is, otherwise it returns False.
        Note: The function should give up and return False if
        the try_number reaches the number of slots in the table.
        At this stage we definitely know we are in a never ending
        cycle and will never find the item...
        You can call this method using Python's 'in' keyword:
            ht = HashTable()
            ...
            if 'foo' in ht:
                ...
        """
        current_index = self._hash(item)
        try_number = 0
        # ---start student section---
        while self._data[current_index] != item:
            if self._data[current_index] == item:
                return True
            elif try_number + 1 >= self.n_slots // 2:
                return False
            try_number += 1
            current_index = (current_index + try_number**2) % self.n_slots
        return True
        
        # ===end student section===

    def __repr__(self):
        output = 'QuadraticOpenAddressHashTable:\n'
        for i in range(self.n_slots):
            output += 'slot {0:8d} = '.format(i)
            item = self._data[i]
            if item == None:
                output = output + '-'
            else:
                output = output + str(item)
            output += '\n'
        load_factor = float(self.n_items)/self.n_slots
        output += 'n_slots = {0:d}\n'.format(self.n_slots)
        output += 'n_items in table = {0:d}\n'.format(self.n_items)
        output += 'Load factor = {0:6.3f}\n'.format(load_factor)
        return output