class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        if not s:
            return res
        d = defaultdict(int)
        d[s[0]] = 1
        i, j = 0, 0
        while j < len(s) - 1:
            max_char_cnt = max(d.values())
            next_char = s[j + 1]
            next_char_cnt = d[next_char]
            len_substr = j + 1 - i + 1
            if max_char_cnt == next_char_cnt or len_substr - max_char_cnt <= k:
                d[next_char] += 1
                j += 1
                res = max(res, len_substr)
            else:
                d[s[i]] -= 1
                i += 1
        return res


if __name__ == "__main__":
    s = Solution()

