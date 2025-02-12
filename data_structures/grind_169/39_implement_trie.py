class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_end_of_word = True        

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_end_of_word

    def startsWith(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.startsWith("app")) # Output: True
trie.insert("app")
print(trie.search("app"))    