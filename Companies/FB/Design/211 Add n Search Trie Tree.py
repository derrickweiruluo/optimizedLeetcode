'''
1.  WordDictionary() Initializes the object.

2.  void addWord(word) Adds word to the data structure, it can be matched later.
3.  bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["#"] = "#"

    def search(self, word: str) -> bool:
        return self.searchNode(word, self.root)
    
    def searchNode(self, word, node):
        for i, ch in enumerate(word):
            if not ch in node:
                if ch == '.':
                    for child in node:
                        if child != '#' and self.searchNode(word[i + 1:], node[child]):
                            return True
                return False
            else:
                node = node[ch]
        return '#' in node