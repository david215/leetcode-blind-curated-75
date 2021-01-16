import java.util.*;

public class Solution {
    
    static boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (!set.add(num)) {
                return true;
            }
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
