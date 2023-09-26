class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dictionary = defaultdict(list)
        def insert( word) -> None:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.count += 1
        root = TrieNode()
        for word in words:
            insert(word)
        for i,c in enumerate (s):
            dictionary[c].append(i)   
        counter = 0
        curr = root

        def dfs(node,index):
            nonlocal counter
            if len(root.children) == 0:
                return 
            # if node.eofword:
            counter += node.count
            for l in node.children:
                print(l)
                pos = bisect_left(dictionary[l],index+1)
                if pos >= len(dictionary[l]):
                    continue
                dfs(node.children[l],dictionary[l][pos])


        dfs(root,-1)
        return counter