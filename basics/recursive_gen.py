'''
Here we generate a bunch of things using recursion

Author: myou
'''


def buildAllSubsetsHelper(k, n, subset):
    if k == n+1:
        print(subset)
    else:
        subset.append(k)
        buildAllSubsetsHelper(k+1, n, subset)
        subset.pop()
        buildAllSubsetsHelper(k+1, n, subset)


'''
Returns all subsets of {1, 2, ..., n}
'''


def buildAllSubsets(n):
    l = []
    return buildAllSubsetsHelper(1, n, l)


def

'''
Test all of our functions out
'''
buildAllSubsets(4)
