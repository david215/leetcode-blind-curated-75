import java.util.*;

public class Solution {

    static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            int diff = target - val;
            int j = map.getOrDefault(diff, -1);
            if (j != -1) {
                return new int[]{i, j};
            } else {
                map.put(val, i);
            }
        }
        return null; // unreachable; handle compiler error
    }

    public static void main(String[] args) {
        int[] nums = new int[]{2, 7, 11, 15};
        int target = 9;
        // int[] nums = new int[]{3, 2, 4};
        // int target = 6;
        // int[] nums = new int[]{3, 3};
        // int target = 6;
        int[] output = twoSum(nums, target);
        System.out.println(Arrays.toString(output));
    }

}

