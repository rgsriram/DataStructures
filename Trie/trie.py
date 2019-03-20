class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
        self.no_of_children = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for character in word:
            node = current.children.get(character)

            if node is None:
                node = TrieNode()
                current.children[character] = node
                current.no_of_children += 1

            current = node

        current.end_of_word = True

    def delete(self, word):
        self._delete(word, self.root, 0)

    def _delete(self, word, current, index):

        if index == len(word):

            if current.end_of_word is False:
                return False

            return len(current.children.keys()) == 0

        node = current.children.get(word[index])

        if node is None:
            return False

        can_delete = self._delete(word, node, index+1)

        if can_delete:
            current.children.pop(word[index])
            return len(current.children.keys()) == 0

        return False

    def complete_search(self, word):
        current = self.root

        for character in word:
            node = current.children.get(character)

            if node is None:
                return False

            current = node

        return current.end_of_word

    def prefix_search(self, word, top=3):
        matched_words = []

        current = self.root
        _match = None

        for character in word:
            node = current.children.get(character)

            if node is None:
                return -1

            if _match is None:
                _match = character

            else:
                _match += character

            current = node

        return self._partial_search(current, _match, matched_words, top)

    def _partial_search(self, node, _match, matched_words, top):

        if node is None:
            return matched_words

        for k, v in node.children.items():

            matched_words.append("%s%s" % (_match, k))

            if len(matched_words) >= top:
                return matched_words

            self._partial_search(v, _match+k, matched_words, top)

        return matched_words

    def print_trie(self, root):

        for k, v in root.children.items():
            print(k)

            if len(v.children.keys()) == 0:
                return

            self.print_trie(v)


def main():
    words = ["sachin", "sehwag", "mark boucher", "mark waugh", "sriram"]

    trie = Trie()

    for word in words:
        trie.insert(word)

    # print("sachin is present: ", trie.complete_search("sachin"))
    # print("mark waugh is present: ", trie.complete_search("mark waugh"))
    # print("deleting mark waugh: ", trie.delete("mark waugh"))
    # print("mark waugh is present: ", trie.complete_search("mark waugh"))

    print("Partial search", trie.prefix_search("s"))

    # print(trie.print_trie(trie.root))

if __name__ == '__main__':
    main()