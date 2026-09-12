class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(node)->Optional[TreeNode]:
            if node != None:
                right=node.right
                left=node.left
                node.right=left
                node.left=right
                invertNode(left)
                invertNode(right)
        invertNode(root)
        return root
