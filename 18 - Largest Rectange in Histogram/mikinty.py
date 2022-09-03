'''
Largest rectangle in histogram with a stack approach

Something that was hard for me to wrap around was why the following solution
works, so I will prove it formally to cast out any doubts.

Theorem: If we have an algorithm where we have a stack and use the rules:
- For some current element i with height h_i, pop off all elements in the stack
  that have height h_j <= h_i
    - When we pop off the elements, we calculate the areas of the rectangles
      that would've started at the histogram column that we popped off
- Add (i', h_i), where i' = min(i, i_1, ..., i_n) where i_k are the indices of
  the elements popped off the stack
- At the very end, compute the size of rectangles from the elements in the
  stack to the end of the array

Proof: To brute force and count all of the possible rectangles, you would start
at a column, and want to go as far as you can, which means as far right as long
as the subsequent columns are >= the height of the starting column. Doing this
with brute force obviously leads to a \sum_{i=0}^{N-1} N-i number of choices to
try, in which case we'd have a O(N^2) algorithm.

To do better, what we can realize is that, if we have column at the top of the
stack with height h', and the next height is h where h < h', the column h' can
no longer "expand right," since it is limited by h. If we had h >= h', then
this would not be an issue. That means we can calculate the size of the
rectangle that starts at h', since it ends right before the index of the
current column with height h. Therefore, for every every column popped in this
middle iteration, we find the maximum size rectangle that starts at thie
column.

Finally, when we pop off the remaining columns in the stack, we are calculating
the maximum areas of the rectangles starting at those columns as well, since
our stack is now sorted by increasing height, which means every column would
have its largest rectangle be the one that extends the entire width of the
list.

Since we have shown that for every column, we are considering the maximum
rectangle from that column, we will find the maximum rectangle in this method.

Lemma: the time complexity of this algorithm is O(N), and uses O(N) space,
where N is the number of columns in the histogram.

For every column, we do a maximum of 2 operations on it; we add it to the
stack, and we pop it off. We do N-1 comparisons to calculate the maximum
rectangle area. Therefore, the time complexity is O(N).

We can potentially add all columns to the stack, e.g. if they are an increasing
sequence of heights, so we may end up using O(N) space. All other components,
e.g. maxHeight and counters are all constant space.
'''

from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    maxArea = 0

    for i in range(len(heights)):
        currHeight = heights[i]
        minIdx = i

        while len(stack) > 0 and currHeight <= stack[-1][1]:
            minIdx, columnHeight = stack.pop()
            maxArea = max(maxArea, (i - minIdx)*(columnHeight))

        stack.append((minIdx, currHeight))

    while len(stack) > 0:
        minIdx, columnHeight = stack.pop()
        maxArea = max(maxArea, (len(heights) - minIdx)*(columnHeight))

    return maxArea

test_cases = [
    (
        [0],
        0
    ),
    (
        [1],
        1
    ),
    (
        [0, 10, 0, 1000, 1, 0],
        1000
    ),
    (
        [1, 1, 1, 1, 1, 1],
        6
    ),
    (
        [1, 1, 3, 2, 5],
        6
    ),
    (
        [1, 1, 1, 1, 1, 1, 2, 2, 2, 3],
        10
    ),
    (
        [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 0, 1, 1, 1, 3],
        10
    ),
    (
        [1, 1, 1, 5, 3, 6, 1, 1, 2],
        9
    ),
    (
        [1, 1, 100, 100, 1, 1, 101, 99],
        200
    ),
    (
        [400, 200, 0, 0, 0, 20000, 0, 0, 1],
        20000
    ),
    (
        [2,1,5,6,2,3],
        10
    )
]

import logging
logging.basicConfig(level=logging.INFO)

for test in test_cases:
    logging.info(f'Test case: {test[0]}')
    res = largestRectangleArea(test[0])

    assert res == test[1],  f'{res} != {test[1]}'

logging.info('All tests passed')
