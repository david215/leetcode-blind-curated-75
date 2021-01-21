[Problem](https://leetcode.com/problems/valid-parentheses/)

## takeaway
- Finding the right data structure is the key to many problems. 

## take 1
![](img-1.jpg)
- code:
```java
public boolean isValid(String s) {
    Deque<Character> stack = new ArrayDeque<>();
    for (char c : s.toCharArray()) {
        if (stack.isEmpty() || !validMatch(stack.peek(), c)) {
            stack.push(c);
        } else {
            stack.pop();
        }
    }
    return stack.isEmpty();
}

private boolean validMatch(char l, char r) {
    return l == '(' && r == ')'
        || l == '[' && r == ']'
        || l == '{' && r == '}';
}
```
- Result
    - Accepted

