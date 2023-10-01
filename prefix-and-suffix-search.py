class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str,index) -> None:
        curr = self.root
        curr.index = index
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.index = index
        

    def search(self, prefix: str,suffix) -> bool:
        curr = self.root
        word = suffix+"#"+ prefix
        for c in word:
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        return curr.index


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for index , word in enumerate(words):
            temp = word + "#" + word
            for i in range(len(word)):
                self.trie.insert(temp[i:],index)

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(pref,suff)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)