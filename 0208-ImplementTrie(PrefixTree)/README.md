[Problem](https://leetcode.com/problems/implement-trie-prefix-tree/)

## takeaway
- Always check if iteration can yield better space complexity.
- Always consider the cost of string operations.

## take 1
- code:
```python
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        first_char = word[:1]
        if first_char not in self.d:
            self.d[first_char] = Trie()
        if word == first_char:  # last char
            self.d[first_char].end = True
        else:
            self.d[first_char].insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        first_char = word[:1]
        if first_char not in self.d:
            return False
        elif word == first_char:  # last char
            return self.d[first_char].end
        else:
            return self.d[first_char].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        first_char = prefix[:1]
        if first_char not in self.d:
            return False
        elif prefix == first_char:  # last char
            return True
        else:
            return self.d[first_char].startsWith(prefix[1:])
```
- Result
    - Accepted
- Note
    - Time Complexity
        - O(S^2) because of slicing.
    - Space Complexity
        - O(S) for operations because of recursive call stacks.

## take 2
- code:
```python
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
```
- Result
    - Accepted
- Note
    - Time Complexity
        - O(S)
    - Space Complexity
        - O(1) for operations.
        - O(S) obviously for the trie itself.

