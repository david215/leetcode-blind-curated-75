import java.util.*;

public class Solution {
    
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

    public static void main(String[] args) {
        System.out.println();
    }

}
