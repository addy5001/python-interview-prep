from tree import BinarySearchTree


def main():
    bst = BinarySearchTree()

    # Populate the tree
    for val in [15, 10, 20, 8, 12, 17, 25]:
        bst.insert(val)

    for val in bst:
        print(val)


if __name__ == "__main__":
    main()
