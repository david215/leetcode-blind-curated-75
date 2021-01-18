[Problem](https://leetcode.com/problems/missing-number/)

## takeaway
- Reducing the elements of an array / collection can reveal useful info.

## take 1
![](img.jpg)
- submission:
```java
public int missingNumber(int[] nums) {
    int n = nums.length;
    int totalSum = n;
    int inputSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum += i;
        inputSum += nums[i];
    }
    return totalSum - inputSum;
}
```
- Time
    - O(N)
- Space
    - O(1)
- Result
    - Accepted
    - using XOR instead of sum is also viable

