class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        max_length = 0
        d = {}
        i = 0
        for j, c in enumerate(s):  # j is the upper bound of the sliding window
            if c in d:
                k = d[c]
                for ch in s[i:k]:
                    del d[ch]
                i = k + 1  # start AFTER the repeated character
            d[c] = j
            max_length = max(max_length, j - i + 1)
        return max_length


if __name__ == "__main__":
    s = Solution()

