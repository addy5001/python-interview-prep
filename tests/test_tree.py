import unittest

from tree import BinarySearchTree, BinarySearchTreeNode, IsBSTCheckMode, ReconstructFrom


class TestBinarySearchTree(unittest.TestCase):
    def _build(self, values):
        t = BinarySearchTree()
        for v in values:
            t.insert(v)
        return t

    # --- Insert ---

    def test_insert_empty(self):
        t = BinarySearchTree()
        t.insert(10)
        self.assertEqual(list(t), [10])

    def test_insert_multiple(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(list(t), [2, 3, 4, 5, 6, 7, 8])

    def test_insert_duplicate(self):
        t = self._build([5, 3, 5])
        self.assertEqual(list(t), [3, 5])

    # --- Remove ---

    def test_remove_leaf(self):
        t = self._build([5, 3, 7])
        t.remove(3)
        self.assertEqual(list(t), [5, 7])

    def test_remove_node_with_left_child(self):
        t = self._build([5, 3, 2])
        t.remove(3)
        self.assertEqual(list(t), [2, 5])

    def test_remove_node_with_right_child(self):
        t = self._build([5, 3, 4])
        t.remove(3)
        self.assertEqual(list(t), [4, 5])

    def test_remove_node_with_two_children(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        t.remove(5)
        self.assertEqual(list(t), [2, 3, 4, 6, 7, 8])

    def test_remove_root_leaf(self):
        t = self._build([5])
        t.remove(5)
        self.assertEqual(list(t), [])

    def test_remove_root_with_left_child(self):
        t = self._build([5, 3])
        t.remove(5)
        self.assertEqual(list(t), [3])

    def test_remove_root_with_right_child(self):
        t = self._build([5, 7])
        t.remove(5)
        self.assertEqual(list(t), [7])

    def test_remove_root_with_two_children(self):
        t = self._build([5, 3, 7])
        t.remove(5)
        self.assertEqual(list(t), [3, 7])

    def test_remove_non_existent(self):
        t = self._build([5, 3, 7])
        with self.assertRaises(ValueError):
            t.remove(99)

    # --- DFS Traversals ---

    def test_inorder(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(list(t.inorder()), [2, 3, 4, 5, 6, 7, 8])

    def test_preorder(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(list(t.preorder()), [5, 3, 2, 4, 7, 6, 8])

    def test_postorder(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(list(t.postorder()), [2, 4, 3, 6, 8, 7, 5])

    def test_empty_traversals(self):
        t = BinarySearchTree()
        self.assertEqual(list(t.inorder()), [])
        self.assertEqual(list(t.preorder()), [])
        self.assertEqual(list(t.postorder()), [])

    # --- is_bst ---

    def test_is_bst_empty(self):
        t = BinarySearchTree()
        self.assertTrue(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertTrue(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    def test_is_bst_single_node(self):
        t = self._build([5])
        self.assertTrue(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertTrue(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    def test_is_bst_valid(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        self.assertTrue(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertTrue(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    def test_is_bst_left_subtree_violation(self):
        t = self._build([5, 3, 7])
        t.root.left.value = 10
        self.assertFalse(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertFalse(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    def test_is_bst_right_subtree_violation(self):
        t = self._build([5, 3, 7])
        t.root.right.value = 1
        self.assertFalse(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertFalse(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    def test_is_bst_deep_violation(self):
        t = self._build([10, 5, 15, 3, 7, 12, 20])
        t.root.left.right.value = 100
        self.assertFalse(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertFalse(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    def test_is_bst_duplicate_violation(self):
        t = self._build([5, 3, 7])
        t.root.right.value = 5
        self.assertFalse(t.is_bst(IsBSTCheckMode.LINEAR))
        self.assertFalse(t.is_bst(IsBSTCheckMode.LOGARITHMIC))

    # --- BFS Traversal ---

    def test_bfs(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(list(t.bfs()), [5, 3, 7, 2, 4, 6, 8])

    def test_empty_tree(self):
        t = BinarySearchTree()
        self.assertEqual(list(t), [])
        self.assertEqual(list(t.bfs()), [])

    # --- Mirror ---

    def test_mirror_empty(self):
        t = BinarySearchTree()
        t.to_mirror()
        self.assertEqual(list(t), [])

    def test_mirror_single_node(self):
        t = self._build([5])
        t.to_mirror()
        self.assertEqual(list(t.bfs()), [5])

    def test_mirror_balanced(self):
        t = self._build([2, 1, 3])
        t.to_mirror()
        self.assertEqual(list(t.bfs()), [2, 3, 1])

    def test_mirror_left_heavy(self):
        t = self._build([3, 2, 1])
        t.to_mirror()
        self.assertEqual(list(t.bfs()), [3, 2, 1])

    def test_mirror_right_heavy(self):
        t = self._build([1, 2, 3])
        t.to_mirror()
        self.assertEqual(list(t.bfs()), [1, 2, 3])

    def test_mirror_larger_tree(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        t.to_mirror()
        self.assertEqual(list(t.bfs()), [5, 7, 3, 8, 6, 4, 2])

    def test_mirror_inorder_reversed(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        original = list(t)
        t.to_mirror()
        self.assertEqual(list(t), list(reversed(original)))

    def test_mirror_twice_is_identity(self):
        t = self._build([5, 3, 7, 2, 4, 6, 8])
        original = list(t.bfs())
        t.to_mirror()
        t.to_mirror()
        self.assertEqual(list(t.bfs()), original)


class TestReconstruct(unittest.TestCase):
    def _build(self, values):
        t = BinarySearchTree()
        for v in values:
            t.insert(v)
        return t

    def _check(self, mode, values):
        """Build a BST, take its traversal, reconstruct, and verify inorder matches."""
        original = self._build(values)
        expected = list(original.inorder())

        if mode in (ReconstructFrom.PREORDER, ReconstructFrom.PREORDER_O_N):
            traversal = list(original.preorder())
        else:
            traversal = list(original.postorder())

        reconstructed = BinarySearchTree().reconstruct(traversal, mode)
        self.assertEqual(list(reconstructed.inorder()), expected)

    # --- Empty ---

    def test_preorder_empty(self):
        r = BinarySearchTree().reconstruct([], ReconstructFrom.PREORDER)
        self.assertEqual(list(r.inorder()), [])

    def test_postorder_empty(self):
        r = BinarySearchTree().reconstruct([], ReconstructFrom.POSTORDER)
        self.assertEqual(list(r.inorder()), [])

    def test_preorder_o_n_empty(self):
        r = BinarySearchTree().reconstruct([], ReconstructFrom.PREORDER_O_N)
        self.assertEqual(list(r.inorder()), [])

    def test_postorder_o_n_empty(self):
        r = BinarySearchTree().reconstruct([], ReconstructFrom.POSTORDER_O_N)
        self.assertEqual(list(r.inorder()), [])

    # --- Single node ---

    def test_preorder_single(self):
        self._check(ReconstructFrom.PREORDER, [42])

    def test_postorder_single(self):
        self._check(ReconstructFrom.POSTORDER, [42])

    def test_preorder_o_n_single(self):
        self._check(ReconstructFrom.PREORDER_O_N, [42])

    def test_postorder_o_n_single(self):
        self._check(ReconstructFrom.POSTORDER_O_N, [42])

    # --- Two nodes (left child) ---

    def test_preorder_two_left(self):
        self._check(ReconstructFrom.PREORDER, [5, 3])

    def test_postorder_two_left(self):
        self._check(ReconstructFrom.POSTORDER, [5, 3])

    def test_preorder_o_n_two_left(self):
        self._check(ReconstructFrom.PREORDER_O_N, [5, 3])

    def test_postorder_o_n_two_left(self):
        self._check(ReconstructFrom.POSTORDER_O_N, [5, 3])

    # --- Two nodes (right child) ---

    def test_preorder_two_right(self):
        self._check(ReconstructFrom.PREORDER, [3, 5])

    def test_postorder_two_right(self):
        self._check(ReconstructFrom.POSTORDER, [3, 5])

    def test_preorder_o_n_two_right(self):
        self._check(ReconstructFrom.PREORDER_O_N, [3, 5])

    def test_postorder_o_n_two_right(self):
        self._check(ReconstructFrom.POSTORDER_O_N, [3, 5])

    # --- Balanced ---

    def test_preorder_balanced(self):
        self._check(ReconstructFrom.PREORDER, [5, 3, 7, 1, 4, 6, 8])

    def test_postorder_balanced(self):
        self._check(ReconstructFrom.POSTORDER, [5, 3, 7, 1, 4, 6, 8])

    def test_preorder_o_n_balanced(self):
        self._check(ReconstructFrom.PREORDER_O_N, [5, 3, 7, 1, 4, 6, 8])

    def test_postorder_o_n_balanced(self):
        self._check(ReconstructFrom.POSTORDER_O_N, [5, 3, 7, 1, 4, 6, 8])

    # --- Left-skewed ---

    def test_preorder_left_skewed(self):
        self._check(ReconstructFrom.PREORDER, [5, 4, 3, 2, 1])

    def test_postorder_left_skewed(self):
        self._check(ReconstructFrom.POSTORDER, [5, 4, 3, 2, 1])

    def test_preorder_o_n_left_skewed(self):
        self._check(ReconstructFrom.PREORDER_O_N, [5, 4, 3, 2, 1])

    def test_postorder_o_n_left_skewed(self):
        self._check(ReconstructFrom.POSTORDER_O_N, [5, 4, 3, 2, 1])

    # --- Right-skewed ---

    def test_preorder_right_skewed(self):
        self._check(ReconstructFrom.PREORDER, [1, 2, 3, 4, 5])

    def test_postorder_right_skewed(self):
        self._check(ReconstructFrom.POSTORDER, [1, 2, 3, 4, 5])

    def test_preorder_o_n_right_skewed(self):
        self._check(ReconstructFrom.PREORDER_O_N, [1, 2, 3, 4, 5])

    def test_postorder_o_n_right_skewed(self):
        self._check(ReconstructFrom.POSTORDER_O_N, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

