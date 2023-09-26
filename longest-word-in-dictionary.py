class TrieNode:
    def __init__(self):
        self.children = {}
        self.eofword = False
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        def insert( word) -> None:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.eofword = True

        for word in words:
            insert(word)
        arr = ""
        def dfs(root,word):
            nonlocal arr
            
            if len(word) > len(arr):
                arr = word
                
            elif len(word) == len(arr) and word < arr:
                arr = word
                
            
            for letter in root.children:
                if root.children[letter].eofword:
                    dfs(root.children[letter],word + letter)
           
        dfs(root,"")

        return arr