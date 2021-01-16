[Problem](https://leetcode.com/problems/????)

## takeaway
- 

![](img.jpg)

## take 1
- two strings are anagrams when they contain the same number of characters
- submission:
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) {
        return false;
    }
    int[] arr = new int[26];
    for (int i = 0; i < s.length(); i++) {
        int j = s.charAt(i) - 'a';
        int k = t.charAt(i) - 'a';
        arr[j] += 1;
        arr[k] -= 1;
    }
    for (int count : arr) {
        if (count != 0) {
            return false;
        }
    }
    return true;
}
```
- Time
    - linear, since sweeping the strings once
- Space
    - constant, since only extra memory used is for an array of length 26
- Result
    - Accepted
    - however, inefficient in both time and space
    - there should be a better solution...

