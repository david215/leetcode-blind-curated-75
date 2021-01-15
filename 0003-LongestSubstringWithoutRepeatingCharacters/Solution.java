import java.util.*;

public class Solution {
    
    static int lengthOfLongestSubstring(String s) {
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

    public static void main(String[] args) {
        String s1 = "abcabcbb";
        String s2 = "bbbbb";
        String s3 = "pwwkew";
        String s4 = "bacab";
        int o1 = lengthOfLongestSubstring(s1);
        int o2 = lengthOfLongestSubstring(s2);
        int o3 = lengthOfLongestSubstring(s3);
        int o4 = lengthOfLongestSubstring(s4);
        System.out.println(o1);
        System.out.println(o2);
        System.out.println(o3);
        System.out.println(o4);
    }

}
