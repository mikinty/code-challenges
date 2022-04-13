'''
Dyanmic Programming

Author: mikinty
'''


def findMinNumberOfCoins(value, coins):
    '''
    Find the minimum number of coins where c \in coins such that
    \sum_{c' \in coins} c' = value.

    Let us assume that all coin values are positive, distinct, and value is also nonegative.

    value: the value to add up to
    coins: positive valued coins, no duplicates
    '''

    recurrence = [None for i in range(value + 1)]

    for i in range(len(recurrence)):
        for c in coins:
            if i - c >= 0:
                if recurrence[i] == None:
                    recurrence[i] = 1 + recurrence[i - c]
                else:
                    recurrence[i] = min(recurrence[i], 1 + recurrence[i - c])
        # No solutions
        if recurrence[i] == None:
            recurrence[i] = 0

    return recurrence[-1]


print([findMinNumberOfCoins(x, [1, 3, 4]) for x in range(20)])
