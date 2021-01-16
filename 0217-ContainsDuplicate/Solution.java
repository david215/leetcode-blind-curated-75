import java.util.*;

public class Solution {
    
    static boolean containsDuplicate(int[] nums) {
        if (nums == null || nums.length == 1) {
            return false;
        }
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int n : nums) {
            max = Math.max(max, n);
            min = Math.min(min, n);
        }
        int diff = max - min;
        if (diff == 0) {
            return true;
        }
        int[] arr = new int[diff + 1];
        for (int n : nums) {
            int i = n - min;
            if (arr[i] != 0) {
                return true;
            }
            arr[i]++;
        }
        return false;
    }

    public static void main(String[] args) {
        List<int[]> inputs = new ArrayList<>();
        List<Boolean> expected = new ArrayList<>();

        inputs.add(new int[]{1, 2, 3, 1});
        expected.add(true);

        inputs.add(new int[]{1, 2, 3, 4});
        expected.add(false);

        for (int i = 0; i < inputs.size(); i++) {
            int[] input = inputs.get(i);
            System.out.println("input: " + Arrays.toString(input));
            System.out.println("expected: " + expected.get(i));
            System.out.println("actual: " + containsDuplicate(input));
            System.out.println();
        }
    }

}
