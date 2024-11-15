class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.is_end_of_word:
                return False
            
        if node.children:
            return False
        node.is_end_of_word = True
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    t = Trie()
    valid = True
    for j in range(n):
        number = input()
        inserted = t.insert(number)
        if inserted is False:
            valid = False
    print("YES") if valid else print("NO")


