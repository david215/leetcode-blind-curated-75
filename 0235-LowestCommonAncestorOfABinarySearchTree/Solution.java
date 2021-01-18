import java.util.*;

public class Solution {
    
    static TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
        while (true) {
            if (p.val < root.val && q.val < root.val) {
                root = root.left;
            } else if (p.val > root.val && q.val > root.val) {
                root = root.right;
            } else {
                break;
            }
        }
        return root;
    }

    public static void main(String[] args) {
        System.out.println();
    }

}
