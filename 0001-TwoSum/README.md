[Problem](https://leetcode.com/problems/two-sum/)

## useful info
- each input has exactly one solution
    - no multiple solutions
    - no no-solution
- cannot use same element twice
    - same element identified by the index, not the value
    - dulicate element allowed, e.g. [3, 3]
- can return the answer in any order

## thougth process
- brute force approach would have a time complexity of O(n^2)
- for each element, if we can determine whether the difference of the element
  is in `nums` in O(1), we can reduce the time complexity to O(n)
- we can meet the above requirement by inserting the difference between each
  element and the `target` as the key and the index of the element as the value
  while iterating over `nums`

## edge cases
- since we know there exists exactly one solution for each input, we don't have
  to handle malformed or invalid input
- we are iterating through the `nums` array only once and we're looking at
  every element, so there seems to be no danger of off-by-one error
- since the order of the indices of the pair does not matter, nothing to handle
  there either

## submission 1
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int val = nums[i];
        int diff = target - val;
        int j = map.getOrDefault(diff, -1);
        if (j != -1) {
            return new int[]{i, j};
        } else {
            map.put(val, i);
        }
    }
    return null; // unreachable; handle compiler error
}
```
- Time
    - O(n) as analyzed above.
- Space
    - O(n), because the additional map requires O(n) space.
- Result
    - Accepted

## take 2
```python
def two_sum(self, nums: list[int], target: int) -> list[int]:
    d = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in d:
            j = d[complement]
            return [i, j]
        else:
            d[n] = i
```
- Result
    - Accepted

