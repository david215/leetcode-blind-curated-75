[Problem](https://leetcode.com/problems/longest-increasing-subsequence/)

## takeaway
- One of the harder DP problems that has a rather creative way of manipulating
  subprolems.

## take 1
- code:
```python
def lengthOfLIS(self, nums: List[int]) -> int:
    l = len(nums)
    dp = [1] * l
    for i in range(1, l):
        dp[i] = 1 + max(dp[j] if nums[j] < nums[i] else 0 for j in range(i))
    return max(dp)
```
- Time
    - O(N^2)
- Space
    - O(N)
- Result
    - Accepted
- Note
    - Not optimal...

## take 2
- code:
```python
def lengthOfLIS(self, nums: List[int]) -> int:
    def binary_search(x: int) -> int:
        i, j = 0, len(dp) - 1
        while i <= j:
            m = (i + j) // 2
            if x < dp[m]:
                j = m - 1
            elif x > dp[m]:
                i = m + 1
            else:
                return m
        return i

    dp = []
    for num in nums:
        i = binary_search(num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)
```
- Time
    - O(N log N)
- Space
    - O(N)
- Result
    - Accepted

