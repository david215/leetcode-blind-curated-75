import java.util.*;

public class Solution {
    
    static ListNode reverseList(ListNode head) {
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

    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static void main(String[] args) {
        ListNode in = new ListNode(1, 
                          new ListNode(2,
                              new ListNode(3,
                                  new ListNode(4, 
                                      new ListNode(5)))));
        ListNode out = reverseList(in);

        ListNode ptr = out;
        while (ptr != null) {
            System.out.println(ptr.val);
            ptr = ptr.next;
        }
    }

}
