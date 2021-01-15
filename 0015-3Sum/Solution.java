import java.util.*;

public class Solution {
    
    static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        int len = nums.length;
        int i = 0;
        while (i < len - 2) {
            if (i > 0) {
                while (i < len - 2 && nums[i - 1] == nums[i]) { i++; }
            }
            int x = nums[i];
            int j = i + 1;
            int k = len - 1;
            while (j < k) {
                int y = nums[j];
                int z = nums[k];
                int threeSum = x + y + z;
                if (threeSum == 0) {
                    result.add(List.of(x, y, z));
                    j++;
                    k--;
                    while (j < k && nums[j - 1] == nums[j]) { j++; }
                    while (j < k && nums[k + 1] == nums[k]) { k--; }
                } else if (threeSum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
            i++;
        }
        return result;
    }

    public static void main(String[] args) {
        List<int[]> inputs = new ArrayList<>();
        List<List<List<Integer>>> expected = new ArrayList<>();

        inputs.add(new int[]{-1, 0, 1, 2, -1, 4});
        expected.add(List.of(List.of(-1, -1, 2), List.of(-1, 0, 1)));

        inputs.add(new int[]{});
        expected.add(List.of());

        inputs.add(new int[]{0});
        expected.add(List.of());

        inputs.add(new int[]{1, 0, -1, -1});
        expected.add(List.of(List.of(1, 0, -1)));

        inputs.add(new int[]{2, 0, -1, -1});
        expected.add(List.of(List.of(2, -1, -1)));

        inputs.add(new int[]{0, 0, 0, 0});
        expected.add(List.of(List.of(0, 0, 0)));

        inputs.add(new int[]{3, 0, -2, -1, 1, 2});
        expected.add(List.of(List.of(-2, -1, 3),
                             List.of(-2, 0, 2), 
                             List.of(-1, 0, 1)));

        inputs.add(new int[]{-1, -1, -1, 0, 0, 0, 1, 1, 1});
        expected.add(List.of(List.of(-1, 0, 1), List.of(0, 0, 0)));

        for (int i = 0; i < inputs.size(); i++) {
            int[] input = inputs.get(i);
            System.out.println(Arrays.toString(input));
            System.out.println(expected.get(i));
            System.out.println(threeSum(input));
            System.out.println();
        }
    }

}
