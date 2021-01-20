import java.util.*;

public class Solution {
    
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) { // t is non-null
            return false;
        } else {
            return isSameTree(s, t)
                || isSubtree(s.left, t)
                || isSubtree(s.right, t);
        }
    }

    private boolean isSameTree(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        } else if (s == null || t == null) {
            return false;
        } else {
            return s.val == t.val
                && isSameTree(s.left, t.left)
                && isSameTree(s.right, t.right);
        }
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
