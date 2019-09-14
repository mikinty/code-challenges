# Challenge 11 - Good Views

Suppose you have a bunch of buildings in a line with heights indicated from
left to right in an array, and there is a beautiful view on the right of all
the buildings.

We define a building as being able to see the view if it can see over all
buildings to its right. So for example, if we had

```python
[1, 12, 3, 5, 4]
```

then the buildings at index `1, 3, 4` can see the view.

Write a function that returns the indices of all buildings that
can see the view.
