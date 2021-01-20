import java.util.*;

public class Solution {
    
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        int prev = nums[len - 1]; // last element
        int max = prev;
        for (int i = len - 2; i >= 0; i--) { // starting at second to last element
            int curr = nums[i];
            if (prev > 0) {
                curr += prev;
            }
            prev = curr;
            max = Math.max(max, curr);
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
