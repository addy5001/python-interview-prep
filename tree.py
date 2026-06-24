import collections
import enum
from collections.abc import Iterator


class BinarySearchTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: BinarySearchTreeNode | None = None
        self.right: BinarySearchTreeNode | None = None

    def __repr__(self) -> str:
        return f"{self.value!r}"


class IsBSTCheckMode(enum.Enum):
    LINEAR = 0
    LOGARITHMIC = 1


class ReconstructFrom(enum.Enum):
    PREORDER = 0
    POSTORDER = 1
    PREORDER_O_N = 2
    POSTORDER_O_N = 3


class BinarySearchTree:
    def __init__(self, node: BinarySearchTreeNode | None = None) -> None:
        self.root: BinarySearchTreeNode | None = node

    def insert(self, value) -> None:
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
            return

        self._insert_value(value, self.root)

    def _insert_value(self, value: int, node: BinarySearchTreeNode) -> None:
        if value == node.value:
            return

        if value < node.value:
            if node.left is None:
                node.left = BinarySearchTreeNode(value)
                return
            self._insert_value(value, node.left)
        else:
            if node.right is None:
                node.right = BinarySearchTreeNode(value)
                return
            self._insert_value(value, node.right)

    def _inorder(self, node: BinarySearchTreeNode | None) -> Iterator[int]:
        if node is None:
            return

        yield from self._inorder(node.left)
        yield node.value
        yield from self._inorder(node.right)

    def inorder(self) -> Iterator[int]:
        yield from self._inorder(self.root)

    def _preorder(self, node: BinarySearchTreeNode | None) -> Iterator[int]:
        if node is None:
            return

        yield node.value
        yield from self._preorder(node.left)
        yield from self._preorder(node.right)

    def preorder(self) -> Iterator[int]:
        yield from self._preorder(self.root)

    def _postorder(self, node: BinarySearchTreeNode | None) -> Iterator[int]:
        if node is None:
            return

        yield from self._postorder(node.left)
        yield from self._postorder(node.right)
        yield node.value

    def postorder(self) -> Iterator[int]:
        yield from self._postorder(self.root)

    def bfs(self) -> Iterator[int]:
        if self.root is None:
            return

        queue = collections.deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            yield node.value

    def dfs(self) -> Iterator[int]:
        if not self.root:
            return

        stack = collections.deque([self.root])
        while stack:
            node = stack.popleft()
            yield node.value
            if node.right:
                stack.appendleft(node.right)
            if node.left:
                stack.appendleft(node.left)

    def is_bst(self, check_mode: IsBSTCheckMode) -> bool:
        match check_mode:
            case IsBSTCheckMode.LINEAR:
                return self._is_bst_sorted_list_check()
            case IsBSTCheckMode.LOGARITHMIC:
                return self._is_bst_min_max_bound_check(
                    self.root, float("-inf"), float("inf")
                )
            case _:
                raise ValueError("Not a valid check mode")

    def _is_bst_sorted_list_check(self) -> bool:
        elements = list(self.inorder())
        if len(elements) <= 1:
            return True

        for i in range(len(elements) - 1):
            if elements[i] >= elements[i + 1]:
                return False

        return True

    def _is_bst_min_max_bound_check(
        self, node: BinarySearchTreeNode | None, min: float, max: float
    ) -> bool:
        if not node:
            return True

        if node.value <= min or node.value >= max:
            return False

        return self._is_bst_min_max_bound_check(
            node.left, min, node.value
        ) and self._is_bst_min_max_bound_check(node.right, node.value, max)

    def remove(self, value) -> None:
        self._remove(value, self.root, None)

    def _remove(
        self,
        value,
        node: BinarySearchTreeNode | None,
        parent: BinarySearchTreeNode | None,
    ) -> None:
        (node_to_remove, parent) = self._find_node(value, node, parent)
        if node_to_remove is None:
            raise ValueError(f"{value!r} does not exist in the tree!")

        if node_to_remove.right is None:
            if parent is None:
                self.root = node_to_remove.left
            else:
                if node_to_remove is parent.left:
                    parent.left = node_to_remove.left
                else:
                    parent.right = node_to_remove.left
        elif node_to_remove.left is None:
            if parent is None:
                self.root = node_to_remove.right
            else:
                if node_to_remove is parent.left:
                    parent.left = node_to_remove.right
                else:
                    parent.right = node_to_remove.right
        else:
            node_to_remove.value = self._pop_min(node_to_remove.right, node_to_remove)

    def _pop_min(
        self,
        node: BinarySearchTreeNode,
        parent: BinarySearchTreeNode,
    ) -> int:
        if node.left is None:
            if node is parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
            return node.value
        return self._pop_min(node.left, node)

    def _find_node(
        self,
        value,
        node: BinarySearchTreeNode | None,
        parent: BinarySearchTreeNode | None,
    ) -> tuple[BinarySearchTreeNode | None, BinarySearchTreeNode | None]:
        if node is None:
            return (None, parent)

        if node.value == value:
            return (node, parent)

        if value < node.value:
            return self._find_node(value, node.left, node)
        else:
            return self._find_node(value, node.right, node)

    def __iter__(self):
        yield from self._inorder(self.root)

    def to_mirror(self) -> None:
        self._to_mirror(self.root)

    def _to_mirror(self, node: BinarySearchTreeNode | None) -> None:
        if node is None:
            return

        self._to_mirror(node.left)
        self._to_mirror(node.right)

        node.left, node.right = node.right, node.left

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, BinarySearchTree):
            return False

        return self._is_subtree(self.root, value.root)

    def is_subtree(self, other: BinarySearchTreeNode | None) -> bool:
        if other is None:
            # Open to interpretation: considering False in this case
            return False

        inner_root = self._find_node_from_value(self.root, other.value)
        if inner_root is None:
            return False

        return self._is_subtree(inner_root, other)

    def _find_node_from_value(
        self, node: BinarySearchTreeNode | None, other_value: int
    ) -> BinarySearchTreeNode | None:
        if node is None:
            return None

        if node.value == other_value:
            return node

        if other_value < node.value:
            return self._find_node_from_value(node.left, other_value)
        else:
            return self._find_node_from_value(node.right, other_value)

    def _is_subtree(
        self, current: BinarySearchTreeNode | None, other: BinarySearchTreeNode | None
    ) -> bool:
        if current is None and other is None:
            return True

        if current is None or other is None:
            return False

        return (
            current.value == other.value
            and self._is_subtree(current.left, other.left)
            and self._is_subtree(current.right, other.right)
        )

    def reconstruct(
        self, element_array: list[int], reconstruct_from: ReconstructFrom
    ) -> BinarySearchTree:
        if not element_array:
            return BinarySearchTree()

        match reconstruct_from:
            case ReconstructFrom.PREORDER:
                return BinarySearchTree(
                    self._reconstruct_from_preorder(
                        element_array,
                        0,
                        len(element_array) - 1,
                    )
                )
            case ReconstructFrom.POSTORDER:
                return BinarySearchTree(
                    self._reconstruct_from_postorder(
                        element_array, len(element_array) - 1, 0
                    )
                )
            case ReconstructFrom.PREORDER_O_N:
                return BinarySearchTree(
                    self._reconstruct_from_preorder_O_n(
                        element_array, float("-inf"), float("inf")
                    )
                )
            case ReconstructFrom.POSTORDER_O_N:
                return BinarySearchTree(
                    self._reconstruct_from_postorder_O_n(
                        element_array, float("-inf"), float("inf")
                    )
                )

    def _reconstruct_from_preorder(
        self,
        element_array: list[int],
        index: int,
        position_bound: int,
    ) -> BinarySearchTreeNode | None:
        if index > position_bound:
            return None

        node = BinarySearchTreeNode(element_array[index])

        right_start = next(
            (
                i
                for i in range(index + 1, position_bound + 1)
                if element_array[i] > node.value
            ),
            position_bound + 1,
        )

        node.left = self._reconstruct_from_preorder(
            element_array, index + 1, right_start - 1
        )
        node.right = self._reconstruct_from_preorder(
            element_array, right_start, position_bound
        )

        return node

    def _reconstruct_from_preorder_O_n(
        self, element_array, min_bound, max_bound
    ) -> BinarySearchTreeNode | None:
        index = 0

        def _construct(min_bound, max_bound) -> BinarySearchTreeNode | None:
            nonlocal index
            if index >= len(element_array):
                return None

            val = element_array[index]
            if val <= min_bound or val >= max_bound:
                return None

            node = BinarySearchTreeNode(val)
            index += 1
            node.left = _construct(min_bound, val)
            node.right = _construct(val, max_bound)

            return node

        return _construct(min_bound, max_bound)

    def _reconstruct_from_postorder(
        self, element_array: list[int], index: int, position_bound: int
    ) -> BinarySearchTreeNode | None:
        if index < position_bound:
            return None

        node = BinarySearchTreeNode(element_array[index])

        leftStart = next(
            (
                i
                for i in range(index - 1, position_bound - 1, -1)
                if element_array[i] < node.value
            ),
            position_bound - 1,
        )

        node.right = self._reconstruct_from_postorder(
            element_array, index - 1, leftStart + 1
        )
        node.left = self._reconstruct_from_postorder(
            element_array, leftStart, position_bound
        )

        return node

    def _reconstruct_from_postorder_O_n(
        self, element_array: list[int], min_bound, max_bound
    ) -> BinarySearchTreeNode | None:
        index = len(element_array) - 1

        def _construct(min_bound, max_bound) -> BinarySearchTreeNode | None:
            nonlocal index

            if index < 0:
                return None

            val = element_array[index]
            if val <= min_bound or val >= max_bound:
                return None

            node = BinarySearchTreeNode(val)
            index -= 1

            node.right = _construct(val, max_bound)
            node.left = _construct(min_bound, val)

            return node

        return _construct(min_bound, max_bound)
