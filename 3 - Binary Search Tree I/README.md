# Challenge 3 - BST I
Recursion and especially BSTs seem to be a hot topic for recruiters. 

Our question is given a binary search tree T, and a number N, find the node with closest value to N (absolute value).

e.g. Given
```
T = Node(
      Node(
        Empty,
        5,
        Empty,
      ),
      10,
      Node(
        Node(
          Empty,
          20,
          Empty,
        ),
        30,
        Empty,
      ),
    )
```

You should get the following results:

```
getClosest(T, 1) = Node(Empty, 5, Empty)
getClosest(T, 10) = T
getClosest(T, 19) = Node(Empty, 20, Empty)
getClosest(T, 1000) = Node(Node(Empty, 20, Empty), 30, Empty)
```