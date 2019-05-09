class EarliestAncestorTests(unittest.TestCase):
￼     def setUp(self):
￼         root = TreeNode(3)
￼         left = TreeNode(4)
￼         right = TreeNode(5)
￼         left_left = TreeNode(1)
￼         left_right = TreeNode(2)
￼
￼         root.left = left
￼         root.right = right
￼         root.left.left = left_left
￼         root.left.right = left_right
￼
￼         t_root = TreeNode(4)
￼         t_left = TreeNode(1)
￼         t_right = TreeNode(2)
￼
￼         t_root.left = t_left
￼         t_root.right = t_right
￼
￼         print Solution(root)
￼
￼ if __name__ == '__main__':
￼     unittest.main() 