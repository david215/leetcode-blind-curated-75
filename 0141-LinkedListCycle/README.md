[Problem](https://leetcode.com/problems/linked-list-cycle/)

## takeaway
- Floyd's cycle detection algorithm.

## take 1
![](img-1.jpg)
- code:
```java
public boolean hasCycle(ListNode head) {
    ListNode tortoise = head;
    ListNode hare = head;
    while (hare != null && hare.next != null) {
        tortoise = tortoise.next;
        hare = hare.next.next;
        if (tortoise == hare) {
            return true;
        }
    }
    return false;
}
```
- Result
    - Accepted

