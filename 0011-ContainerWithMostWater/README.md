[Problem](https://leetcode.com/problems/container-with-most-water/)

## useful info
- heights are non-negative integers
    - non-negative, so the height can be 0
- there are at least 2 height values in the input array
- you may not slant the container... which would be a more challenging problem
  anyway

## thought process
- naive brute force approach would look at all possible pairs of indices, where
  there are O(n^2) such pairs
- computation of the area is going to take constant time, so the overall time
  complexity of the brute force approach is going to be quadratic
- we probably are looking for something in linear or linearithmic time
- is there a data structure we can leverage on to reduce the time complexity?
- the max area between two bars is the product of the distance between the
  bars, i.e. the difference between the two indices, and the height of the
  shorter bar of the two
- two pointer technique seems suitable for solving the problem
- where can each pointer start at? try the first and the last indices
- for each pointer, if the "next" bar is taller than the current move the
  pointer towards the other pointer
    - could it be possible to reduce the maxArea by taking this approach?
    - what if the height difference is only 1?
    - e.g. {1, 2, 1}
        - the maxArea will decrease from 2 to 1...
        - what should be the criteria for moving the pointer correctly?
        - maybe we can just compute the maxArea using the next bar and decide?
    - e.g. {1, 1, 10, 5}
        - moving either of the pointer will not yield greater area...
        - maybe move the pointer if maxArea doesn't decrease?
    - e.g. {10, 0, 9, 0, 1}
        - moving the rightmost most pointer twice yields the maxArea, but how
          do we determine this?
- let's approach the quesiton with a recursive perspective
- the max area between i and j is one of the followings:
    1. the area between i and j
    2. the max area between (i + 1) and j
    3. the max area between i and (j - 1)
- what's the time complexity of this approach though?
- branching factor of 2 and the height of the tree is n, not log n, so O(n^2)
- however, we could memoize redundant computations
- taking the recursion approach, a helper fucntion with indices as param migth
  prove useful
- memoization doesn't change the fact that there are O(n^2) pairs and also
  requires O(n^2) space... not optimal!
- back to two pointer technique...
- let's think about the relationship between max area between i and j vs max
  area between (i + 1) and j, or similarly, i and (j - 1)
- if there is no bar taller than either of the bars at i and j between i and j,
  we've already achieved the max possible area
- but if there is at least one bar taller than either of the bars at i and j,
  it is possible that moving the pointer could yield greater max area.
- we've seen in the case of {1, 2, 1} that moving the pointer just because the
  next bar is taller isn't good enough
- e.g. {10, 0, 9, 0, 1}
    - since 9 > 1, moving j from 4 to 2 increases the area
    - however, if there are multiple such bars, how do we handle them?
- e.g. {1, 2, 3, 2, 1}
    - max area is 4, can be either between the 1s or the 2s
- e.g. {1, 3, 5, 3, 1}
    - max area is 6 between the 3s
- what if for each bar between i and j that is taller, say at index k, we
  compute the area between (i, k), (k, j), and compare with the area between
  (i, j)?
- there can be O(n) such bars even at the worst case
- checking for each height, however, will also be O(n) so the overall time
  complexity will be quadratic if we can't improve the approach somehow
- instead, maybe we can compare the height of the bars at i and j to determine
  which pointer to move
- there are 3 cases:
    1. height[i] > height[j]
        - area between (i, j) > area between(i + 1, j)
        - but does that mean we must decrement j?
        - e.g. {10, 1, 1, 1, 5}, keeping i and j yields the max area
        - e.g. {10, 1, 10, 1, 3}, moving j yields the max area
        - then how do we determine when to move a pointer?
    2. height[i] < height[j]
        - area between (i, j) > area between(i, j - 1)
    3. height[i] == height[j]
        - ...?
- my pitfall was that I was so fixated by the idea of keeping the two pointers
  stay at the indices that would yield the max area, instead of recording the
  computed area at those indices and moving on
- also, I had a misconception of what moving a pointer is; what does it mean to
  *move a pointer* in this problem? it means we will skip **all** the pairs
  with the old index because we're no longer interested in them
- so the approach of trying to "move" a pointer to find greater max area is
  completely backwards
- back to the 3 cases:
    1. height[i] > height[j]
        - for all k such that i < k < j, area(i, k) < area(i, j)
        - i.e. "moving" j to the left will never increase the area with fixed i
        - that means we are no longer interested with **any** of the pairs with
          i in them
        - that is, we can "move" the pointer, i.e. increment i, and move on
    2. height[i] < height[j]
        - for all k such that i < k < j, area(k, j) < area(i, j)
        - applying the same logic, we can decrement j and move on
    3. height[i] == height[j]
        - area(i, k) < area(i, j) and area(k, j) < area(i, j) for all k!
        - we can increment i and also decrement j!
- now coding the above idea is simple


## edge cases
- all values can be 0, then the maxArea is also 0

## submission 1
```java
public int maxArea(int[] height) {
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
```
- Time
    - O(n), because the condition i < j will be met in linear time with the two
      pointers approaching each other from the ends
- Space
    - O(1), because no additional data structure or recursion
- Result
    - Accepted

## submission 2
```python
def maxArea(self, height: List[int]) -> int:
    res = 0
    i = 0
    j = len(height) - 1
    while i < j:
        x = height[i]
        y = height[j]
        w = j - i
        h = min(x, y)
        res = max(res, w * h)
        if x < y:
            i += 1
        elif x > y:
            j -= 1
        else:
            i += 1
            j -= 1
    return res
```
- Time
    - O(N)
- Space
    - O(1)
- Result
    - Accepted

