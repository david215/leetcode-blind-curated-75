import java.util.*;

public class Solution {
    
    static String longestPalindrome(String s) {
        String result = "";
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        for (int k = 0; k < len; k++) {
            for (int i = 0; i < len - k; i++) {
                int j = i + k;
                if (i == j) {
                    dp[i][j] = true;
                } else if (i + 1 == j) {
                    dp[i][j] = s.charAt(i) == s.charAt(j);
                } else {
                    dp[i][j] = dp[i + 1][j - 1] && s.charAt(i) == s.charAt(j);
                }
                if (dp[i][j] && j - i + 1 > result.length()) {
                    result = s.substring(i, j + 1); // upper-bound exclusive
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String s1 = "babad";
        String s2 = "cbbd";
        String s3 = "a";
        String s4 = "ac";
        String s5 = "abbaxyz";
        String s6 = "xyzaba";
        String s7 = "abcdefedcba";
        String o1 = longestPalindrome(s1);
        String o2 = longestPalindrome(s2);
        String o3 = longestPalindrome(s3);
        String o4 = longestPalindrome(s4);
        String o5 = longestPalindrome(s5);
        String o6 = longestPalindrome(s6);
        String o7 = longestPalindrome(s7);
        System.out.println("Expected: " + "bab, Actual: " + o1);
        System.out.println("Expected: " + "bb, Actual: " + o2);
        System.out.println("Expected: " + "a, Actual: " + o3);
        System.out.println("Expected: " + "a, Actual: " + o4);
        System.out.println("Expected: " + "abba, Actual: " + o5);
        System.out.println("Expected: " + "aba, Actual: " + o6);
        System.out.println("Expected: " + "abcdefedcba, Actual: " + o7);
    }

}
