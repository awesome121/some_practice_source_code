import re
import os
from time import clock, perf_counter
import doctest




def _c_mul(value_a, value_b):
    '''Substitute for c multiply function'''
    return ((int(value_a) * int(value_b)) & 0xFFFFFFFF)



def nice_hash(input_string):
    '''Takes a string name and returns a hash for the string. This hash value
    will be os independent, unlike the default Python hash function.'''
    if input_string is None:
        return 0 # empty
    value = ord(input_string[0]) << 7
    for char in input_string:
        value = _c_mul(1000003, value) ^ ord(char)
    value = value ^ len(input_string)
    if value == -1:
        value = -2
    return value





#---------------------------------------------
# Start of Class definitions
#---------------------------------------------
class ChainingHashTable():
    """A simple HashTable.
    ***** IMPORTANT
    ***** =========
    ***** NOTE: These will fail initially, ie, when _hash returns 0
    ***** DON'T worry you will fix this later:)
    >>> hash_table = ChainingHashTable(5)
    >>> hash_table.store('George')
    >>> hash_table.store('Bungle')
    >>> hash_table.store('Zippy')
    >>> hash_table.store('Jane')
    >>> hash_table.store('Rod')
    >>> hash_table.store('Freddy')
    >>> print(hash_table)
    ChainingHashTable:
    slot        0 = ['Rod']
    slot        1 = ['George', 'Jane']
    slot        2 = ['Bungle']
    slot        3 = ['Zippy', 'Freddy']
    slot        4 = []
    n_slots = 5
    n_items in table = 6
    Load factor =  1.200
    Average chain length = 1.200
    <BLANKLINE>
    NOTE: ChainingHashTable print doctests will fail initially, ie, when _hash returns 0
    Don't worry you will fix this later... See handout
    <BLANKLINE>
    >>> print('Freddy' in hash_table)
    True
    >>> print('Dipsy' in hash_table)
    False
    """

    def __init__(self, slots=11):
        """
        Creates a new hashtable with a number of slots (default: 11).
        It will help if you always make your hash table size a prime number.

        Each slot will contain a list of items that hash to the slot.
        Initially the list in each slot contains a None.
        n_items contains the number of items that have been put in the table.
        """
        self._data = [[] for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0

    def _hash(self, item):
        """Computes the hash of an item.
        First calculate using nice_hash(item) and then use modulo
        to reduce it down to a number in the range 0..slef.n_slots """
        # NOTE:
        # We will use a trivial hash function here to start with
        # Don't worry, you will get to update it later in the lab...
        return nice_hash(item) % self.n_slots

    def store(self, item):
        """Appends an item to the list in the slot at _data[hash]."""
        index = self._hash(item)
        self._data[index].append(item)
        # Keep track of number of items in hash table
        self.n_items += 1

    def average_chain_length(self):
        """ Returns the average chain length """
        return self.n_items / self.n_slots

    def __str__(self):
        output = 'ChainingHashTable:\n'.format(self.n_slots)
        for i in range(self.n_slots):
            list_at_slot = self._data[i]
            output = output+'slot {0:8d} = '.format(i)
            if list_at_slot == None:
                output = output + 'None'
            else:
                output = output + str(list_at_slot)
            output += '\n'
        load_factor = float(self.n_items)/self.n_slots
        output += 'n_slots = {0:d}\n'.format(self.n_slots)
        output += 'n_items in table = {0:d}\n'.format(self.n_items)
        output += 'Load factor = {0:6.3f}\n'.format(load_factor)
        output += 'Average chain length = {0:.3f}\n'.format(self.average_chain_length())
        output += '\n'
        output += 'NOTE: ChainingHashTable print doctests will fail initially, ie, when _hash returns 0\n'
        output += "Don't worry you will fix this later... See handout\n"
        return output

    def __contains__(self, item):
        """
        Checks to see if an item is stored within the hashtable.
        Returns True if it does, otherwise it returns False.
        You can call this method using Python's 'in' keyword:
            ht = HashTable()
            ...
            if 'foo' in ht:
            ...
        """
        # remember self._data[index] contains a list of items that hash to
        # the slot at the given index
        # ---start student section---
        index = self._hash(item)
        for data in self._data[index]:
            if data == item:
                return True
        return False
        # ===end student section===






#----------------------------------------------------------------------------
class LinearHashTable():
    """A simple Open Addressing HashTable with Linear Probing.
    Called simply LinearHashTable to make the name shorter...

    >>> hash_table = LinearHashTable(11)
    >>> hash_table.store('Paul')
    >>> hash_table.store('Peter')
    >>> hash_table.store('Paula')
    >>> hash_table.store('David')
    >>> hash_table.store('Bobby')
    >>> hash_table.store('Dianna')
    >>> print(hash_table)
    LinearHashTable:
    slot        0 = David
    slot        1 = Paul
    slot        2 = -
    slot        3 = -
    slot        4 = Peter
    slot        5 = Paula
    slot        6 = -
    slot        7 = -
    slot        8 = -
    slot        9 = Bobby
    slot       10 = Dianna
    n_slots = 11
    n_items in table = 6
    Load factor =  0.545
    <BLANKLINE>
    >>> print('Peter' in hash_table)
    True
    >>> print('Dingus' in hash_table)
    False
    """
    def __init__(self, slots=11):
        """
        Creates a new hashtable with the given number of slots.
        Remember we can't have a load factor greater than 1 for an open hash...
        """
        self._data = [None for i in range(slots)]
        self.n_slots = slots
        self.n_items = 0


    def store(self, item):
        """Stores an item in the hashtable."""
        if self.n_slots == self.n_items:
            #Argh - crash, who made the hashtable too small?
                print(self._data)
                print('Size = ' + str(self.n_slots))
                print('Slots used = ' + str(self.n_items))
                print("Whoops, hash table is full!!!!")
                print("In reality you would have made it bigger by now...")
                print("But, you're not expected to for this lab.")
                raise IndexError ("Hash table is full!!!!")
        # ***********************************************************
        # ---start student section---
        index = self._hash(item)
        if self._data[index] is not None:
            count = 1
            while self._data[index] is not None:
                index = (self._hash(item) + count) % self.n_slots
                count += 1
        self._data[index] = item
            
        # ===end student section===

        # Keep track of number of items in hash table
        self.n_items += 1

    def _hash(self, item):
        """Computes the hash of an item."""
        return nice_hash(item) % self.n_slots

    def __contains__(self, item):
        """
        Checks to see if an item is stored within the hashtable.
        Returns True if it does, otherwise it returns False.
        You can call this method using Python's 'in' keyword:
            ht = HashTable()
            ...
            if 'foo' in ht:
                ...
        """
        first_hash = self._hash(item)
        have_wrapped = False
        if self._data[first_hash] == item:
            return True
        else:
            current_index = first_hash
            while self._data[current_index] is not None:
                if self._data[current_index] == item:
                    # horay we found it
                    return True
                if (current_index == first_hash) and have_wrapped:
                        # back to original hash and didn't find item
                        # phew - the hashtable is full!
                        return False
                if current_index == (self.n_slots-1):
                        # wrap back to start of hash table
                        current_index = 0
                        have_wrapped = True
                else:
                    current_index += 1

    def __str__(self):
        """ Returns a string representation of the hashtable
        Along with some summary stats.
        """
        output = 'LinearHashTable:\n'
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





#----------------------------------------------------------------------------
class QuadraticHashTable():
    """Is a child class of OpenAddressHashTable.
    If a collision then uses a quadratic probing function to find a free slot
    >>> hash_table = QuadraticHashTable(11)
    >>> hash_table.store('Paul')
    >>> hash_table.store('Peter')
    >>> hash_table.store('Paula')
    >>> hash_table.store('David')
    >>> hash_table.store('Bobby')
    >>> hash_table.store('Dianna')
    >>> hash_table.store('Dirk')
    >>> hash_table.store('Darlene')
    >>> print(hash_table)
    QuadraticOpenAddressHashTable:
    slot        0 = David
    slot        1 = Paul
    slot        2 = Darlene
    slot        3 = -
    slot        4 = Peter
    slot        5 = Paula
    slot        6 = Dirk
    slot        7 = -
    slot        8 = -
    slot        9 = Bobby
    slot       10 = Dianna
    n_slots = 11
    n_items in table = 8
    Load factor =  0.727
    <BLANKLINE>
    >>> print('Dirk' in hash_table)
    True
    >>> print('Dingle' in hash_table)
    False
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
#==============================================











def load_dict_words(filename):
    """
    Load a dictionary from a file, and returns a list of all words in the
    dictionary.
    Dictionary files should have one word per line.
    """
    with open(filename, 'r', encoding = 'latin_1') as file:
        words = [line.strip().lower() for line in file]
    return words



def load_doc_words(filename):
    """
    Loads a document from a file, and returns a list of all words in the
    document. 'Words' are sequences of one or more [A-Za-z] characters.
    Words are converted to lowercase.
    """
    with open(filename, 'r', encoding = 'ascii') as file:
        words = [word.lower() for word in re.findall(r'[A-Za-z]+', file.read())]
    return words







#----------------------------------------------------------------------------
def spellcheck_with_list(document, dictionary_word_list, quiet_mode=False):
    """
    Checks the spelling of each word in 'document' (a list of words from a text)
    against the dictionary_word_list (the list of correct words).
    """
    #Check all words in the document list
    #Printing out misspelled words and counting them
    if not quiet_mode:
        print('-----------------')
        print('Misspelled words:')
        print('-----------------')
    num_errors = 0
    unique_errors = set()  # hint hint :)
    start_check_time = perf_counter()

    # ***********************************************************
    # Write your spell check code here
    # ---start student section---
    for word in document:
        if word in unique_errors:
            num_errors += 1
        elif word not in dictionary_word_list:
            print(word)
            num_errors += 1
            unique_errors.add(word)
    # ===end student section===
    end_check_time = perf_counter()
    check_time = end_check_time - start_check_time
    ms_per_word = (check_time/len(document))*1000
    if not quiet_mode:
        print('-'*50)
        print('Number of errors = {0:d} words'.format(num_errors))
        print('='*50+'\n')
        print('-------------------------------------------')
        print('Summary stats (using simple linear search):')
        print('-------------------------------------------')
        print('Words in dictionary = {0:d} words'.format(len(dictionary_word_list)))
        print('Input file length = {0:d} words'.format(len(document)))
        print('Document check time = {0:8.4f}s'.format(check_time))
        print('Check time per word in document = ', end='')
        print('{0:10.6f}ms\n\n'.format(ms_per_word))
    return check_time



#----------------------------------------------------------------------------
def build_hash_table(ht_type, ht_size, dictionary_word_list, quiet_mode=False):
    """ Stores all the dictionary words in a hash table of the
    given type and size.
    Returns the hash table and the time taken to build it
    """
    #Build Hash Table by adding words from the dictionary word list
    start_build_time = perf_counter()
    if ht_type == 'Chaining':
        hash_table = ChainingHashTable(ht_size)
    elif ht_type == 'Linear':
        hash_table = LinearHashTable(ht_size)
    elif ht_type == 'Quadratic':
        hash_table = QuadraticHashTable(ht_size)
    else:
        print('Hash type must be Chaining, Linear or Quadratic.')
    for word in dictionary_word_list:
        hash_table.store(word)
    end_build_time = perf_counter()
    build_time = end_build_time - start_build_time
    return hash_table, build_time




#----------------------------------------------------------------------------
def spellcheck_with_hashtable(document,
                              dictionary_word_list,
                              ht_type,
                              ht_size,
                              quiet_mode=False):
    """
    Checks the spelling of each word in 'document' (a list of words) against
    the dictionary (another list of words, using the given hash_table).

    """
    hash_table, build_time = build_hash_table(ht_type, ht_size, dictionary_word_list)

    #Check all words in the document list
    #Printing out misspelled words and counting them
    if not quiet_mode:
        print('-----------------')
        print('Misspelled words:')
        print('-----------------')
    num_errors = 0
    start_check_time = perf_counter()
    unique_errors = set()  # hint hint :)

    # ***********************************************************
    # Write your spell check code here
    # ---start student section---
    for word in document:
        if word in hash_table:
            num_errors += 1
        elif word not in dictionary_word_list:
            print(word)
            num_errors += 1
            hash_table.store(word)
    # ===end student section===
    end_check_time = perf_counter()
    check_time = end_check_time - start_check_time
    load_factor = float(hash_table.n_items)/hash_table.n_slots
    ms_per_word = (check_time/len(document))*1000
    if not quiet_mode:
        print('-'*50)
        print('Number of errors = {0:d} words'.format(num_errors))
        print('='*50)
        print()
        print('-'*50)
        print('Summary stats (using '+ht_type+' hash table):')
        print('-'*50)
        print('Words in dictionary = {0:d} words'.format(len(dictionary_word_list)))
        print('Hash table size = {0:d} slots'.format(hash_table.n_slots))
        print('Hash table load factor = {0:8.4f}'.format(load_factor))
        print('Hash table build time = {0:8.4f}s'.format(build_time))
        print('Input file length = {0:d} words'.format(len(document)))
        print('Document check time = {0:8.4f}s'.format(check_time))
        print('Check time per word in document = ', end='')
        print('{0:10.6f}ms\n\n'.format(ms_per_word))
    return  check_time




def binary_search(values, needle):
    lowerBound = 0
    upperBound = len(values)
    index = 0
    # ---start student section---
    pass
    # ===end student section===
    return False



# ------------------------------------------------
def spellcheck_bin(document, dictionary, quiet_mode=False):
    #Check all words in the document list
    #Printing out misspelled words and counting them
    if not quiet_mode:
        print('-----------------')
        print('Misspelled words:')
        print('-----------------')
    num_errors = 0

    dict_sort_start = perf_counter()
    dictionary = sorted(dictionary)
    dict_sort_end = perf_counter()

    start_check_time = perf_counter()
    for word in document:
        if not binary_search(dictionary, word):
            if not quiet_mode: print(word)
            num_errors += 1
    end_check_time = perf_counter()
    check_time = end_check_time - start_check_time
    ms_per_word = (check_time/len(document))*1000
    dict_sort_time = dict_sort_end - dict_sort_start
    if not quiet_mode:
        print('-'*50)
        print('Number of errors = {0:d} words'.format(num_errors))
        print('='*50+'\n')
        print('--------------------------------------------------')
        print('Summary stats (using Binary Search on Dictionary):')
        print('--------------------------------------------------')
        print('Input file length = {0:d} words'.format(len(document)))
        print('Dictionary sort time = {0:8.4f}s'.format(dict_sort_time))
        print('Document check time = {0:8.4f}s'.format(check_time))
        print('Check time per word in document = ', end='')
        print('{0:10.6f}ms\n\n'.format(ms_per_word))
    return check_time





if __name__ == '__main__':
    # you don't need to worry about what the next line does :
    os.environ['TERM'] = 'linux' # Suppress ^[[?1034h to keep doctests happy


    # Idividual tests:
    doctest.run_docstring_examples(ChainingHashTable, None)
    doctest.run_docstring_examples(LinearHashTable, None)
    doctest.run_docstring_examples(QuadraticHashTable, None)

    # run all the doctests:
    # doctest.testmod()


    # NOTE:
    # Use tester.py to do some test runs with hash tables and
    # to do some spellchecks on various files



