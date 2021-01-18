import java.util.*;

public class Solution {
    
    static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p == null || q == null) {
            return false;
        } else {
            return p.val == q.val
                && isSameTree(p.left, q.left)
                && isSameTree(p.right, q.right);
        }
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
