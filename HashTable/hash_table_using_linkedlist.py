from LinkedList.linkedlist import LinkedList


class HashTableUsingLL(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.linked_list = LinkedList()

    def _put(self, key, value):
        _hash = self._hash(key)

        if self.slots[_hash] is not None:
            head = self.slots[_hash]

        else:
            head = self.linked_list.head

        self.slots[_hash] = self.linked_list.insert(head, "%s || %s || %s" % (key, _hash, value))

    def _get(self, key):
        _hash = self._hash(key)

        if self.slots[_hash] is None:
            raise Exception('No key is present')

        head = self.slots[_hash]
        value = self.linked_list.contains(head, "%s || %s" % (key, _hash))

        if not value:
            raise Exception('Error in retrieval')

        return value.split('||')[2].strip()

    def _hash(self, key):
        return key % self.size

    def __setitem__(self, key, value):
        self._put(key, value)

    def __getitem__(self, key):
        return self._get(key)