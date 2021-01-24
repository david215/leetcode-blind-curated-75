[Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## useful info
- `s` consists of English letters, digits, symbols, and spaces
- there can be multiple substrings of the same maximum length

## thought process
- naive brute force approach: start with character and continue until meeting a
  repeating chracter, keeping track of the maximum length, e.g. for "abcabcbb",
  ("a", len = 1) -> ("ab", len = 2) -> ("abc", len = 3) -> repetition, but
  remember the maximum length of 3 -> ("b", len = 3) -> ... and so on
    - this approach is O(n^2), as it requires n + (n - 1) + (n - 2)... lookups
- is there a data structure I can leverage on to reduce to O(n)? O(n log n)?
- when we encounter "abca", we want to start with "bca", not "b"; if this is
  possible, we can achieve O(n)
- keep track of start and end index?
- and a accompanying set of some sort to keep track of character repetition?
- however, in the case of "baca", we need to skip 2 chracters and move on to
  "ca", which means a simple set won't suffice
- we need to use a map to store the index
- when we skip multiple letters, we need to modify/delete some entries in the
  map, e.g. "baca" will drop char b.
- alternatively, we can check `lastIndex` and if it is not between i and j,
  ignore accordingly; this method will require less compute.

## edge cases
- for an empty string, i.e. "", return 0
- for a single character string, return 1
    - same for the repeated, e.g. "bbbbb"
- "bacab" should return 3, where the longest substring is "bac" and "cab"

## submission 1
```java
public int lengthOfLongestSubstring(String s) {
    int max = 0;
    int i = 0;
    Map<Character, Integer> map = new HashMap<>();
    for (int j = 0; j < s.length(); j++) {
        char c = s.charAt(j);
        int lastIndex = map.getOrDefault(c, -1);
        if (lastIndex != -1 && lastIndex >= i) {
            i = lastIndex + 1;
        }
        map.put(c, j);
        max = Math.max(max, j - i + 1);
    }
    return max;
}
```
- Time
    - O(n) since we are iterating through the string once and get and put
      operations on a hash map is O(1)
- Space
    - O(n) for the additional map
- Result
    - Accepted

## take 2
```python
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
```
- Result
    - Accepted

