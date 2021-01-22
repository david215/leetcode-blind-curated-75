import java.util.*;

public class Solution {
    
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numToCountMap = new HashMap<>();
        for (int num : nums) {
            numToCountMap.put(num, numToCountMap.getOrDefault(num, 0) + 1);
        }
        
        Map<Integer, Set<Integer>> countToNumsMap = new HashMap<>();
        int maxCount = 0;
        for (Map.Entry<Integer, Integer> e : numToCountMap.entrySet()) {
            int num = e.getKey();
            int count = e.getValue();
            Set<Integer> set = countToNumsMap.get(count);
            if (set == null) {
                set = new HashSet<>();
                countToNumsMap.put(count, set);
            }
            set.add(num);
            maxCount = Math.max(maxCount, count);
        }

        int[] result = new int[k];
        int i = 0;
        int j = maxCount;
        while (i < k && j >= 0) {
            if (countToNumsMap.containsKey(j)) {
                for (int num : countToNumsMap.get(j)) {
                    result[i++] = num;
                }
            }
            j--;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
