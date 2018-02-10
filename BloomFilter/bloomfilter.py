import mmh3
import math
from bitarray import bitarray


class BloomFilter(object):
    def __init__(self, n, p=None, m=None, k=None):
        self.size = n

        self.bit_array_size = m or self._get_bit_array_size(self.size, p)
        self.hash_count = k or self._get_hash_count(self.bit_array_size, self.size)
        self.fp = p or self._get_false_positive(self.size, self.hash_count, self.bit_array_size)

        self.bit_array = bitarray(self.bit_array_size)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            self.bit_array[digest] = True

    def is_exists(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            if self.bit_array[digest] is False:
                return False

        return True

    @classmethod
    def _get_hash_count(cls, m, n):
        return int((m/n) * math.log(2))

    @classmethod
    def _get_bit_array_size(cls, n, p):
        return int(-(n * math.log(p))/(math.log(2)**2))

    @classmethod
    def _get_false_positive(cls, n, k, m):
        return (1 - ((1 - (1/m)) ** (k * n))) ** k
