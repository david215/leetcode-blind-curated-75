import java.util.*;

public class Solution {
    
    static int climbStairs(int n) {
        if (n < 3) {
            return n;
        }
        int prev = 1;
        int curr = 2;
        for (int i = 3; i <= n; i++) {
            int tmp = curr;
            curr = prev + curr;
            prev = tmp;
        }
        return curr;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
