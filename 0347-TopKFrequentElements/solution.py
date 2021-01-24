class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        bins = [None for _ in range(len(nums))]
        for key, val in c.items():
            if not bins[val - 1]:
                bins[val - 1] = []
            bins[val - 1].append(key)

        res = []
        for i in range(len(nums) - 1, -1, -1):
            curr_bin = bins[i]
            if curr_bin:
                res += curr_bin
                k -= len(curr_bin)
                if k == 0:
                    break
        return res


if __name__ == "__main__":
    s = Solution()

