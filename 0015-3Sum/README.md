[Problem](https://leetcode.com/problems/3sum/)

## takeaway
- Sorting an array can add nice properties to aid solving the problem.
- Handling unordered duplicates can be quite a challenge, because it is hard to
  leverage on hash-based uniqueness check and using sets.
- Sometimes the solution does require handling tricky stuff, like the
  not-so-simple duplicate skipping logic in this problem.
- Adding custom data structures, although fun, is probably not the way to go.

## useful info
- there can be zero or more solutions
- the solution set must not contain duplicate triplets
    - what does "duplicate" exactly mean? does order matter?
- the order of the elements in the returned triplets doesn't matter
- looking for **unique** triplets
    - e.g. {1, 0, -1, -1} won't return two sets of {1, 0, -1}

## edge cases
- if nums is empty, no solution
- if nums contains less than 3 elements, no solution

## take 1
- how many triplets? O(n^2) if same asymtotics as pairs
- actually there are O(n^3) triplets, because for each pair, you there are
  n - 2, i.e. O(n), third option
- brute force approach then will have a cubic time complexity
- we then are likely looking for something quadratic
- counting the number of each element might prove useful, because we are
  interested in unique triplets
- e.g. {1, 0, -1, -1} will return {{1, 0, -1}}
- e.g. {2, 0, -1, -1} will return {{2, -1, -1}}
- e.g. {0, 0, 0} will return {{0, 0, 0}}
- the above two cases illustrate the 3 cases where duplicate elements are
  treated differently: the first ignores the duplicate, the second uses both,
  the last is an edge of three zeroes
- if there are more than 3 copies of an element, can we safely ignore them?
- recall how TwoSum can be solved in linear time: we used a map and stored the
  complement value as the key and the index as the value
- could we apply a similar approach, storing the sum of pairs as the complement
  as the key and the pair of indices as the value?
- if we could make that work, the overall time complexity will be reduced to
  quadratic as opposed to cubic
- can we handle duplicates gracefully in this approach?
- using a HashSet to check for duplication will fail, unless we can come up
  with a hash function such that a hash of the two triplets are the same when
  they are permutations of each other, but different when they are not
- seems to be more challenging than it appear...
- all valid non-unique triplets will sum to 0, so if we naively use the sum of
  the triplet to be the hash, we will end up with some terrible hash collisions
- but how to make the hash order-indepedent without summing them?
- submission
```java
public List<List<Integer>> threeSum(int[] nums) {
    Set<Triplet> answerSet = new HashSet<>();
    Map<Integer, Set<Pair>> map = new HashMap<>();

    int len = nums.length;
    for (int i = 0; i < len - 1; i++) {
        for (int j = i + 1; j < len; j++) {
            int x = nums[i];
            int y = nums[j];
            int sum = x + y;
            int comp = -sum;
            Set<Pair> set = map.getOrDefault(comp, new HashSet<>());
            set.add(new Pair(i, j));
            map.put(comp, set);
        }
    }

    for (int k = 0; k < len; k++) {
        int z = nums[k];
        Set<Pair> idxPairs = map.get(z);
        if (idxPairs != null) {
            for (Pair idxPair : idxPairs) {
                int i = idxPair.x;
                int j = idxPair.y;
                if (k != i && k != j) {
                    int x = nums[i];
                    int y = nums[j];
                    answerSet.add(new Triplet(x, y, z));
                }
            }
        }
    }

    List<List<Integer>> answer = new ArrayList<>();
    for (Triplet t : answerSet) {
        answer.add(t.toList());
    }
    return answer;
}

static class Pair {
    int x;
    int y;

    Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Pair) {
            Pair op = (Pair) o;
            return this.x == op.x && this.y == op.y
                || this.x == op.y && this.y == op.x;
        }
        return false;
    }

    @Override
    public int hashCode() {
        return x + y;
    }
}

static class Triplet {
    int x;
    int y;
    int z;

    Triplet(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    List<Integer> toList() {
        return List.of(x, y, z);
    }

    @Override
    public boolean equals(Object o) {
        if (o instanceof Triplet) {
            Triplet ot = (Triplet) o;
            int[] a = new int[]{this.x, this.y, this.z};
            int[] b = new int[]{ot.x, ot.y, ot.z};
            Arrays.sort(a);
            Arrays.sort(b);
            for (int i = 0; i < 3; i++) {
                if (a[i] != b[i]) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    @Override
    public int hashCode() {
        return x + y + z;
    }
}
```
- Result
    - Time Limit Exceeded
    - as expected, using the sum of the elements as the hash of a Triplet
      results in all Triplet objects having the same hash code, and the
      containment check in the HashSet becomes linear as opposed to constant.
    - also, in the worst case scenario, we're going to end up with O(n^3)
      Triplets, so this approach is no good

## take 2
- other approaches...? quadratic? linear? lineararithmic?
- we could sort the array in linearithmic time
- we don't necessarily have to deal with indices...? handling duplication could
  require attention though
- then we can effectively divide the array into 3 portions of negative, zero,
  and positive integers
- if we use a zero, we can pick one negative and one positive integers of the
  same magnitude to form a 3sum
- if we don't use a zero, we can either pick two negatives and a positive
  integer whose sum is 0, or one negative and two positive integers whose sum
  is 0
- e.g. {-1, 0, 1, 2, -1, -4} -> {-4, -1, -1, 0, 1, 2}
- how do we handle duplicates in this case?
- hmm... it seems that the number of occurrence matter... use a HashMap?
```java
public List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> answers = new ArrayList<>();

    Map<Integer, Integer> map = new HashMap<>();
    for (int num : nums) {
        int count = map.getOrDefault(num, 0);
        count++;
        map.put(num, count);
    }

    for (Map.Entry<Integer, Integer> e : map.entrySet()) {
        int num = e.getKey();
        int count = e.getValue();
        if (num == 0) {
            if (count >= 3) {
                answers.add(List.of(0, 0, 0));
            }
        } else if (num > 0) { // handles duplication
            if (map.containsKey(0)) {
                int comp = -num;
                int compCount = map.getOrDefault(comp, 0);
                if (compCount > 0) {
                    answers.add(List.of(0, num, comp));
                }
            }
            if (count >= 2) {
                int doubleComp = -(num * 2);
                int doubleCompCount = map.getOrDefault(doubleComp, 0);
                if (doubleCompCount > 0) {
                    answers.add(List.of(num, num, doubleComp));
                }
            }
            if (num % 2 == 0) {
                int halfComp = -(num / 2);
                int halfCompCount = map.getOrDefault(halfComp, 0);
                if (halfCompCount >= 2) {
                    answers.add(List.of(num, halfComp, halfComp));
                }
            }
        }
    }

    return answers;
}
```
- Result
    - Wrong Answer
        - completely derped out and forgot about the cases like {-2, -1, 3}

## submission 3
- the key problem that I keep encountering is handling the duplicates, i.e.
  differentiating between {-1, 0, 1} and {1, 0, -1}
- maybe it is possible to come up with a clever hash function to handle this?
- but let's go back to the idea of sorting the array first for now
- first of all, sorting the array has linearithmic time complexity, and since
  we're most likely looking for a quadratic solution, it seems sound time
  complexity-wise to sort the array
- when the array is sorted, we can ensure that the elements inside a triplet is
  ordered, and also, skipping duplicate elements is simplified
- however, we should be careful because there are cases where we want two
  occurrences of the same element, e.g. {-1, -1, 2}
- using a two pointer technique, we can iterate over the sorted array, skipping
  elements as needed, to solve the problem in quadratic time
```java
public List<List<Integer>> threeSum(int[] nums) {
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
```
- Time
    - O(n^2), as we are doing O(n) iterations of a two pointer technique where
      each iteration is also O(n)
- Space
    - O(1), as no extra data structure or recursion is used
- Result
    - Accepted

## take 4
- once the array is sorted, it could also be possible to once again apply the
  hash map approach used in Two Sum, because sorting the array, again, helps in
  handling duplicate elements.
```java
static List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(nums);
    int i = 0;
    int len = nums.length;
    while (i < len - 2) {
        twoSum(nums, i, result);
        i++;
        while (i < len - 2 && nums[i - 1] == nums[i]) { i++; }
    }
    return result;
}

static void twoSum(int[] nums, int i, List<List<Integer>> result) {
    int len = nums.length;
    int x = nums[i];
    Map<Integer, Integer> map = new HashMap<>();
    for (int j = i + 1; j < nums.length; j++) {
        int y = nums[j];
        int yCount = map.getOrDefault(y, 0);
        yCount++;
        map.put(y, yCount);
    }
    int j = i + 1;
    while (j < len - 1) {
        int y = nums[j];
        int z = -x - y;
        int zCount = map.getOrDefault(z, 0);
        if (y == z && zCount >= 2) {
            result.add(List.of(x, y, z));
        } else if (y < z && zCount >= 1) {
            result.add(List.of(x, y, z));
        }
        j++;
        while (j < len - 1 && nums[j - 1] == nums[j]) { j++; }
    }
}
```
- Time
    - quadratic, as we perform O(n) twoSum calls where each twoSum call takes
      linear time
- Space
    - linear, as each twoSum call uses O(n) space for the map
- Result
    - Accepted
    - as expected, much slower than the two pointer approach despite the same
      asymptotic time complexity, and uses more space

## take 4
- Python version
- code:
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    end = len(nums) - 1
    i = 0
    while i <= end - 2:
        j = i + 1
        k = end
        a = nums[i]
        while j < k:
            b, c = nums[j], nums[k]
            sum_ = a + b + c
            if sum_ == 0:
                res.append([a, b, c])
                while nums[j] == b and j < k:
                    j += 1
                while nums[k] == c and j < k:
                    k -= 1
            elif sum_ < 0:
                j += 1
            else:  # sum > 0
                k -= 1
        while nums[i] == a and i <= end - 2:
            i += 1
    return res
```
- Time
    - O(N^2)
- Space
    - O(1)
- Result
    - Accepted

