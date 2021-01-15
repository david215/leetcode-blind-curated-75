import java.util.*;

public class Solution {

    static int maxArea(int[] height) {
        int maxArea = 0;
        int i = 0;
        int j = height.length - 1;
        while (i < j) {
            int width = j - i;
            int x = height[i];
            int y = height[j];
            maxArea = Math.max(maxArea, width * Math.min(x, y));
            if      (x < y) { i++;      }
            else if (x > y) { j--;      }
            else            { i++; j--; }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        List<int[]> inputs = new ArrayList<>();
        List<Integer> expected = new ArrayList<>();

        inputs.add(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7});
        expected.add(49);

        inputs.add(new int[]{1, 1});
        expected.add(1);

        inputs.add(new int[]{4, 3, 2, 1, 4});
        expected.add(16);

        inputs.add(new int[]{1, 2, 1});
        expected.add(2);

        inputs.add(new int[]{1, 1, 10, 5});
        expected.add(5);

        inputs.add(new int[]{10, 0, 9, 0, 1});
        expected.add(18);

        inputs.add(new int[]{1, 1, 1, 1, 1});
        expected.add(4);

        inputs.add(new int[]{0, 0, 0, 0, 0});
        expected.add(0);

        inputs.add(new int[]{1, 2, 3, 2, 1});
        expected.add(4);

        inputs.add(new int[]{1, 3, 5, 3, 1});
        expected.add(6);

        inputs.add(new int[]{1, 3, 5, 3, 2});
        expected.add(6);

        inputs.add(new int[]{1, 2, 3, 4, 5});
        expected.add(6);

        inputs.add(new int[]{1, 0, 10, 0, 100, 100, 0, 10, 0, 1});
        expected.add(100);

        for (int i = 0; i < inputs.size(); i++) {
            int[] input = inputs.get(i);
            System.out.println("input: " + Arrays.toString(input));
            System.out.println("expected: " + expected.get(i));
            System.out.println("actual: " + maxArea(input));
            System.out.println();
        }
    }

}
