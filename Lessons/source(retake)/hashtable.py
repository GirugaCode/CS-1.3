#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __iter__(self):
        """Used __iter__ method to optimize space"""
        for bucket in self.buckets:
            for item in bucket.items():
                yield item

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """
        Return the load factor, the ratio of number of entries to buckets.
        Runtime: O(1)
        Condition: returning the ratio in constant time
        """
        # Calculates the load factor which is the probability of an item being in the same bucket
        return self.size / len(self.buckets)

    def keys(self):
        """
        Return a list of all keys in this hash table.
        Runtime: O(n)
        Condition: Iterates through each bucket item and appends the key in the empty list
        """
        # Collect all keys in each of the buckets
        all_keys = []
        for key,value in self:
            all_keys.append(key)
        return all_keys

    def values(self):
        """
        Return a list of all values in this hash table.
        Runtime: O(n)
        Condition: Iterates through each bucket item and appends the value in the empty list
        """
        # Collect all values in each of the buckets
        all_values = []
        for key, value in self:
            all_values.append(value)
        return all_values

    def items(self):
        """
        Return a list of all entries (key-value pairs) in this hash table.
        Runtime: O(n)
        Condition: Iterates through buckets and extends each item
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for item in self:
            all_items.append(item)
        return all_items

    def length(self):
        """
        Return the number of key-value entries by traversing its buckets.
        Runtime: O(n)
        Condition: Iterates through buckets and calculates length
        """
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets:
            item_count += bucket.length()
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """
        Return True if this hash table contains the given key, or False.
        Best Case: O(1)
        Condition: Finds the key in the immediately in the iteration
        Worst Case: O(n)
        Condition: Iterates through the entire list to find the key
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """
        Return the value associated with the given key, or raise KeyError.
        Best Case: O(1)
        Condition: Getting the first index or last index would be constant
        Worst Case: O(n)
        Condition: Iterates through the entire list to get the key
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """
        Insert or update the given key with its associated value.
        Best Case: O(n)
        Worst Case: O(n)
        Condition: Always going to be O(n) time because it will always go through the buckets
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        self.size += 1
        # Call the resize function if the load factor is greater than 0.75
        if self.load_factor() > 0.75:
            self._resize()

    def delete(self, key):
        """
        Delete the given key and its associated value, or raise KeyError.
        Best Case: O(1)
        Worst Case: O(n)
        Condition: Always going to be O(n) time because it will always go through the buckets
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """
        Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).\
        Best Case: O(n)
        Worst Case: O(2n + b)
        Condition: Iterates through self.items and setting the key,value pair
        # Calculating Runtime:
        # O(n) + O(b) + O(n) = O(2n + b) = O(n + b)
        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size
        
        # A list to temporarily hold all current key-value entries
        temp_list = self.items() # O(n) using extend for every item in the buckets

        # Reinitalizes the init when we need to resize our hashtables
        self.__init__(new_size) # O(2b) -> O(b) time and space complexity

        for key, value in temp_list: # O(n) loops through all the entries
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
