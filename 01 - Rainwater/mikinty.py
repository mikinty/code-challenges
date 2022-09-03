'''
Approach 1: Use a stack

The idea here is that we want to keep track of the largest wall to the left of us, and as we sweep from left to right, we know exactly how much water is being trapped by each subsequent component.
The tricky part is that, we have two cases

1. If the current column is shorter than the top of the stack (left tall element), then we just add the contributions immediately.
2. If the current column is larger than the top of the stack, then we add contributions that "haven't been counted yet"
'''

from typing import List

import logging
logging.basicConfig(level=logging.INFO)

def rainWater(heights: List[int]) -> int:
    stack = []
    totalWater = 0

    for i in range(len(heights)):
        height = heights[i]

        if len(stack) > 0:
            heightBarrier = min(height, stack[0][1])
            while len(stack) > 0 and height >= stack[-1][1]:
                idx, h = stack.pop()

                if len(stack) >= 1:
                    width = idx - stack[-1][0]
                    totalWater += width*(heightBarrier - h)
                    logging.debug(f'Add {width} x ({heightBarrier} - {h})')

        stack.append((i, height))
        logging.debug(f'{stack}, totalWater = {totalWater}')

    return totalWater

test_cases = [
    (
        [0],
        0
    ),
    (
        [1],
        0
    ),
    (
        [1, 0, 2, 0, 3, 0, 4],
        6
    ),
    (
        [1, 1, 1, 1, 1, 1],
        0
    ),
    (
        [1, 1, 3, 2, 5],
        1
    ),
    (
        [1, 0, 2, 0, 3, 0, 4, 0, 3, 0, 2, 0, 1],
        12
    ),
    (
        [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 0, 1, 1, 1, 3],
        9
    ),
    (
        [2, 0, 1, 0, 4, 2, 3, 0, 2, 0, 5, 0, 0, 2],
        22
    ),
    (
        [1, 1, 100, 100, 1, 1, 101, 99],
        198
    ),
    (
        [400, 200, 0, 0, 0, 20000, 0, 0, 1],
        1402
    ),
    (
        [2,1,5,6,2,3],
        2
    )
]

for test in test_cases:
    logging.info(f'Test case: {test[0]}')
    res = rainWater(test[0])

    assert res == test[1],  f'{res} != {test[1]}'

logging.info('All tests passed')
