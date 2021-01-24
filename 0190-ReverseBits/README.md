[Problem](https://leetcode.com/problems/reverse-bits/)

## takeaway
- Be careful with off-by-one error, e.g. this problem needed 31 shifts, not 32.

## take 1
![](img-1.jpg)
- code:
```java
public int reverseBits(int n) {
    int reversed = n & 1;
    for (int i = 0; i < 31; i++) {
        n >>>= 1; // unsigned right shift
        reversed <<= 1;
        reversed |= n & 1;
    }
    return reversed;
}
```
- Result
    - Accepted

## take 2
- Python version
- code
```python
def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(31):
        b = n & 1
        res |= b
        n >>= 1
        res <<= 1
    res |= n
    return res
```
- Time
    - O(1)
- Space
    - O(1)
- Result
    - Accepted

