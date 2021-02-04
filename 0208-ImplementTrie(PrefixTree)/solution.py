class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = Trie.TrieNode()
            ptr = ptr.children[c]
        ptr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True


if __name__ == "__main__":
    s = Solution()

