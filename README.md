# Python Interview Prep

A repository containing clean, thoroughly tested Python implementations of core data structures and interview algorithm patterns. Built as reference code and practice materials for technical interviews.

---

## 📂 Repository Structure

- **[list.py](file:///Users/aadhavanramesh/Projects/python-interview-prep/list.py)**: A custom implementation of a singly linked list (`LinkedList`) conforming to Python's abstract base class `MutableSequence`.
- **[tree.py](file:///Users/aadhavanramesh/Projects/python-interview-prep/tree.py)**: An implementation of a `BinarySearchTree` featuring DFS/BFS traversals, validation, deletion, mirroring, and reconstruction algorithms.
- **[main.py](file:///Users/aadhavanramesh/Projects/python-interview-prep/main.py)**: Quick entry point to run and experiment with basic BST operations.
- **[tests/](file:///Users/aadhavanramesh/Projects/python-interview-prep/tests)**: A comprehensive test suite using Python's built-in `unittest` module.

---

## ⚙️ Implemented Data Structures & Algorithms

### 🔗 Singly Linked List (`list.py`)
- Extends `collections.abc.MutableSequence`.
- `insert(index, value)`: Inserts an element at the specified index.
- `__getitem__(index)`: Retrieves an element at a given 0-indexed position.
- `reversed()`: Recursively reverses the list and returns an iterable of elements.

### 🌳 Binary Search Tree (`tree.py`)
- **Traversals**:
  - Breadth-First Search (BFS) using `collections.deque`.
  - Depth-First Search (DFS) iteratively using a stack.
  - Recursive Inorder, Preorder, and Postorder traversals.
- **Validation** (`is_bst`):
  - Linear mode: Extracts inorder traversal and validates sortedness.
  - Logarithmic mode: Performs a single-pass O(N) min/max bound recursive verification.
- **Modification**:
  - `insert(value)`: Inserts a node while maintaining BST properties.
  - `remove(value)`: Deletes a node (handles leaf, single-child, and dual-child nodes via successor replacement).
  - `to_mirror()`: Recursively mirrors the BST (swaps all left and right children).
- **Subtree Verification**:
  - `is_subtree(other_node)`: Checks whether another tree is a subtree of the current BST.
- **Reconstruction**:
  - Reconstructs the exact BST from a list of its traversal values.
  - **Preorder Modes**:
    - `PREORDER`: Scanning boundaries recursively ($O(N^2)$ worst case).
    - `PREORDER_O_N`: Linear-time construction using recursive min/max limits ($O(N)$).
  - **Postorder Modes**:
    - `POSTORDER`: Scanning boundaries recursively ($O(N^2)$ worst case).
    - `POSTORDER_O_N`: Linear-time construction using recursive min/max limits ($O(N)$).

---

## 🛠️ Getting Started & Running Tests

This project requires **Python 3.14+** and is managed with the [uv](https://github.com/astral-sh/uv) package manager.

### Running the entry point
```bash
uv run python3 main.py
```

### Running the tests
To execute all test suites (covering basic operations, traversals, modifications, and reconstruction edge cases):
```bash
uv run python3 -m unittest discover tests -v
```
