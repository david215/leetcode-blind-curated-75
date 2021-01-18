import java.util.*;

public class Solution {
    
    static int missingNumber(int[] nums) {
        int n = nums.length;
        int totalSum = n;
        int inputSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += i;
            inputSum += nums[i];
        }
        return totalSum - inputSum;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
