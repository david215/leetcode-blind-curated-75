import java.util.*;

public class Solution {
    
    static boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (x, y) -> Integer.compare(x[0], y[0]));
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i - 1][1] > intervals[i][0]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<int[][]> inputs = new ArrayList<>();
        List<Boolean> expected = new ArrayList<>();

        inputs.add(new int[][]{{0, 30}, {5, 10}, {15, 20}});
        expected.add(false);

        inputs.add(new int[][]{{7, 10}, {2, 4}});
        expected.add(true);

        inputs.add(new int[][]{});
        expected.add(true);

        inputs.add(new int[][]{{1, 2}});
        expected.add(true);

        for (int i = 0; i <  inputs.size(); i++) {
            int[][] input = inputs.get(i);
            System.out.println("input: " + Arrays.deepToString(input));
            System.out.println("expected: " + expected.get(i));
            System.out.println("actual: " + canAttendMeetings(input));
            System.out.println();
        }
    }

}
