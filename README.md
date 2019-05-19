# PYTHON-BINARY-SEARCH-TREE
A simple binary search tree implementation with rotations, insertions, removal and more.
This is an exercise for a more complex project im working on, that is implementing red black trees with ASCII printing of the nodes.

A binary search tree is a binary tree (every node can have at most 2 children), in which every value that is bigger than a node will get placed in its right side, similarly every value that is smaller than a node will get places in its left side. This is true for **every node and every subtree**


![](https://github.com/FezFamiliar/Web-Vulnerabilities/blob/master/CBC_encryption.png)

In an averagte case, every operation (insertion, deletion, search) can be executed in O(logn), although in the worst case it **linear**.
This happens because the tree gets heavily **imbalanced** and basically it becomes a linked list. We will see soon that improvements can be added so that any tree self balances itself. Thus lowering the complexity to O(logn).

