[Problem](https://leetcode.com/problems/????)

## takeaway
- 

![](img.jpg)

## take 1
- a goofy approach using a map
- not the "right" way to solve the problem, but just wanted to see how it turns
  out
- submission:
```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    Map<Integer, ListNode> map = new HashMap<>();
    int i = 0;
    while (head != null) {
        map.put(i++, head);
        head = head.next;
    }
    int j = i - 1;
    head = map.get(j);
    ListNode ptr = head;
    while (j >= 0) {
        ptr.next = map.get(j--);
        ptr = ptr.next;
    }
    ptr.next = null;
    return head;
}
```
- Time
    - O(N), since only need sweep the linked list once
- Space
    - O(N), because O(N) elements are inserted into the map
- Result
    - Accepted
    - slower than the "right" approach, as expected
    - surprisingly, less memory usage compared to 93.82% of other submissions
      despite linear space complexity, probably because a recursive approach
      require O(N) stack frames anyways

