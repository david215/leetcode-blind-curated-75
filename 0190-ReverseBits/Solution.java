import java.util.*;

public class Solution {
    
    public int reverseBits(int n) {
        int reversed = n & 1;
        for (int i = 0; i < 31; i++) {
            n >>>= 1; // unsigned right shift
            reversed <<= 1;
            reversed |= n & 1;
        }
        return reversed;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
