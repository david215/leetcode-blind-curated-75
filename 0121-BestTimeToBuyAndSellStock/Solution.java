import java.util.*;

public class Solution {
    
    static int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int p : prices) {
            min = Math.min(min, p);
            maxProfit = Math.max(maxProfit, p - min);
        }
        return maxProfit;
    }

    public static void main(String[] args) {
        List<int[]> inputs = new ArrayList<>();
        List<Integer> expected = new ArrayList<>();

        inputs.add(new int[]{7, 1, 5, 3, 6, 4});
        expected.add(5);

        inputs.add(new int[]{7, 6, 4, 3, 1});
        expected.add(0);

        for (int i = 0; i < inputs.size(); i++) {
            int[] input = inputs.get(i);
            System.out.println(Arrays.toString(input));
            System.out.println(expected.get(i));
            System.out.println(maxProfit(input));
            System.out.println();
        }
    }

}
