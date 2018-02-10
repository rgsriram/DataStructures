from bloomfilter import BloomFilter
from random import shuffle

n = 20
k = 4
m = 20

bloomf = BloomFilter(n, m=20, k=k)
print("Size of bit array:{}".format(bloomf.size))
print("False positive Probability:{}".format(bloomf.fp))
print("Number of hash functions:{}".format(bloomf.hash_count))

# words to be added
word_present = ['abound', 'abounds', 'abundance', 'abundant', 'accessable',
                'bloom', 'blossom', 'bolster', 'bonny', 'bonus', 'bonuses',
                'coherent', 'cohesive', 'colorful', 'comely', 'comfort',
                'gems', 'generosity', 'generous', 'generously', 'genial']

# word not added
word_absent = ['bluff', 'cheater', 'hate', 'war', 'humanity',
               'racism', 'hurt', 'nuke', 'gloomy', 'facebook',
               'geeksforgeeks', 'twitter']

for item in word_present:
    bloomf.add(item)

shuffle(word_present)
shuffle(word_absent)

test_words = word_present[:10] + word_absent
shuffle(test_words)
for word in test_words:
    if bloomf.is_exists(word):
        if word in word_absent:
            print("'{}' is a false positive!".format(word))
        else:
            print("'{}' is probably present!".format(word))
    else:
        print("'{}' is definitely not present!".format(word))