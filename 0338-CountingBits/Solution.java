import java.util.*;

public class Solution {
    
    public int[] countBits(int num) {
        int[] result = new int[num + 1];
        result[0] = 0;
        if (num == 0) {
            return result;
        }
        result[1] = 1;
        int powerOfTwo = 1;
        for (int i = 2; i <= num; i++) { // inclusive
            if (i == powerOfTwo << 1) {
                result[i] = 1;
                powerOfTwo <<= 1;
            } else {
                result[i] = 1 + result[i - powerOfTwo];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
