class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            cnt_arr = [0] * 26
            for c in s:
                cnt_arr[ord(c) - ord('a')] += 1
            d[tuple(cnt_arr)].append(s)
        return d.values()

if __name__ == "__main__":
    s = Solution()

