'''
You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.


return top 3, if there is tie, by Lexico order
if less then 3 , return 0-2


Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.
'''


# Clarification:  user at least type a word and end with '#

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.cache_count = dict()
        self.keyword = ""
        for i, sen in enumerate(sentences):
            self._add_word(sen, self.trie)
            self.cache_count[sen] = times[i]

    def _add_word(self, word, trie):
        for char in word:
            if char not in trie.node:
                trie.node[char] = Trie()
            trie = trie.node[char]
            trie.words.append(word)
        return True

    def _find_words(self, word):
        cur = self.trie
        for char in word:
            if char in cur.node:
                cur = cur.node[char]
            else:
                return []
        return cur.words

    def input(self, c):
        if c != '#':
            self.keyword = self.keyword + c
            words = self._find_words(self.keyword)
            res = []
            for word in words:
                res.append((self.cache_count[word], word))
            res = list(set(res))
            return [s[1] for s in sorted(res, key=lambda x: (-x[0], x[1]))[:3]]
        else:
            self.cache_count[self.keyword] = self.cache_count.get(self.keyword,0) +1
            self._add_word(self.keyword,self.trie)            
            self.keyword = ""
        return []