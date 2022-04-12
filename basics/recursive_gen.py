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


def buildAllSubsets(n):
    '''
    Returns all subsets of {1, 2, ..., n}
    '''
    l = []
    return buildAllSubsetsHelper(1, n, l)


def generateAllFullSetsHelper(n, perm):
    if len(perm) == n:
        print(perm)
    else:
        for i in range(1, n+1):
            perm.append(i)
            generateAllFullSetsHelper(n, perm)
            perm.pop()


def generateAllFullSets(n):
    '''
    Return all sets S of length n such that x \in S satisfies x \in {1, ..., n}
    '''
    l = []
    return generateAllFullSetsHelper(n, l)


def generateAllPermutationsHelper(n, perm, chosen):
    if len(perm) == n:
        print(perm)
    else:
        for i in range(1, n+1):
            if not chosen[i]:
                perm.append(i)
                chosen[i] = True
                generateAllPermutationsHelper(n, perm, chosen)
                perm.pop()
                chosen[i] = False


def generateAllPermutations(n):
    '''
    Return all n! ordered permutations of {1, ..., n}
    '''
    l = []
    chosen = {}
    for i in range(1, n+1):
        chosen[i] = False

    return generateAllPermutationsHelper(n, l, chosen)


'''
Test all of our functions out
'''
# buildAllSubsets(4)
# generateAllFullSets(4)
generateAllPermutations(4)
