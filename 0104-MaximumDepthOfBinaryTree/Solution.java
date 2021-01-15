import java.util.*;

public class Solution {

    static int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            int leftDepth = maxDepth(root.left);
            int rightDepth = maxDepth(root.right);
            return 1 + Math.max(leftDepth, rightDepth);
        }
    }

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static void main(String[] args) {
        List<TreeNode> inputs = new ArrayList<>();
        List<Integer> expected = new ArrayList<>();

        inputs.add(null);
        expected.add(0);

        inputs.add(new TreeNode(1));
        expected.add(1);

        inputs.add(new TreeNode(1,
                       null,
                       new TreeNode(1)
                   )
        );
        expected.add(2);

        inputs.add(new TreeNode(1,
                       new TreeNode(1),
                       new TreeNode(1,
                           new TreeNode(1),
                           new TreeNode(1)
                       )
                   )
        );
        expected.add(3);

        for (int i = 0; i < inputs.size(); i++) {
            System.out.println(expected.get(i));
            System.out.println(maxDepth(inputs.get(i)));
            System.out.println();
        }
    }

}
