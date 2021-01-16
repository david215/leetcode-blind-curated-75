import java.util.*;

public class Solution {
    
    static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char x = s.charAt(i);
            char y = t.charAt(i);
            if (x != y) {
                int n = map.getOrDefault(x, 0);
                int m = map.getOrDefault(y, 0);
                map.put(x, n + 1);
                map.put(y, m - 1);
            }
        }
        for (int count : map.values()) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
