'''
largest sum in array
mikinty
'''

TEST_CASES = [
        [0, 1, 2],
        [-3, 1, 4, 5, -4],
        [1, 4, 5, -20, 4, 7, 6, 5, -100],
        [1, 2, 5, -9, 2, 3, 0, -7, 19, 3, 0, -4],
        [-10, 1, 5, 4, 11, -100, 3, 5, 6, 7, 12, 21, -1000, 134]
]

def largest_contiguous_sum(array):
    curr_low = 0
    curr_sum = 0
    curr_max = 0

    for i in range(len(array)):
        curr_sum += array[i]
        if curr_sum < curr_low:
            curr_low = curr_sum
        if curr_sum - curr_low > curr_max:
            curr_max = curr_sum - curr_low

    return curr_max

for i in range(len(TEST_CASES)):
    curr_array = TEST_CASES[i]
    print(largest_contiguous_sum(curr_array), curr_array)
