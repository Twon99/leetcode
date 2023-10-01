class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        #self.flag = False
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c !='.':
                i = ord(c) - ord("a")
            else:
                continue 
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.search_in_node(word, self.root)
    
    def search_in_node(self, word: str, node: TrieNode) -> bool:
        for i, c in enumerate(word):
            if c == '.':
                return any(self.search_in_node(word[i + 1:], child) for child in node.children if child)
            index = ord(c) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.end
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)