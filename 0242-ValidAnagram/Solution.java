import java.util.*;

public class Solution {
    
    static boolean isAnagram(String s, String t) {
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

    public static void main(String[] args) {
        System.out.println();
    }

}
