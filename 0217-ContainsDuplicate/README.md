[Problem](https://leetcode.com/problems/????)

## takeaway
- 

![](img.jpg)

## take 1
- using a set can trivialize this problem
- submission:
```java
public boolean containsDuplicate(int[] nums) {
    Set<Integer> set = new HashSet<>();
    for (int num : nums) {
        if (!set.add(num)) {
            return true;
        }
    }
    return false;
}
```
- Time
    - linear, since sweeping the array once where each insertion takes constant
      time
- Space
    - linear, since allocating a set whose size could grow up to exactly N in
      the case of no duplicate
- Result
    - Accepted
    - can be faster?

