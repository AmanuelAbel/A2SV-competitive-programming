class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr.children[c].count += 1
            curr = curr.children[c]
    def count(self, word: str,count) -> bool:
        curr = self.root
        for c in word:
            count += curr.children[c].count
            curr = curr.children[c]
        return count
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        arr = []
        for i in words:
            print(i)
            root.insert(i)
        for i in words:
            arr.append(root.count(i,0))
        return arr