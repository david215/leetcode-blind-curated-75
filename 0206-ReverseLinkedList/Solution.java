import java.util.*;

public class Solution {

    static ListNode reverseList(ListNode head) {
        ListNode reversed = null;
        while (head != null) {
            ListNode tmp = head.next;
            head.next = reversed;
            reversed = head;
            head = tmp;
        }
        return reversed;
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
