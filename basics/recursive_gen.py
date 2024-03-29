'''
Here we generate a bunch of things using recursion

Author: mikinty
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


def nQueensHelper(row, board):
    if row == len(board):
        for i in range(len(board)):
            print(''.join([str(x) for x in board[i]]))
        print(''.join(['-' for i in range(len(board))]))
    else:
        def inRange(row, col, board):
            return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])

        def noQueensBehind(row, col, board):
            # Check rows behind
            for delta in range(1, row + 1):
                if board[row - delta][col] != 0:
                    return False
                if inRange(row - delta, col - delta, board) and board[row - delta][col - delta] != 0:
                    return False
                if inRange(row - delta, col + delta, board) and board[row - delta][col + delta] != 0:
                    return False

            return True

        for col in range(len(board)):
            if noQueensBehind(row, col, board):
                board[row][col] = 'Q'
                nQueensHelper(row + 1, board)
                board[row][col] = 0


def nQueens(n):
    '''
    Generates all possible nxn boards where n queens do not attack any of
    themselves
    '''
    board = [[0 for j in range(n)] for i in range(n)]

    nQueensHelper(0, board)


'''
Test all of our functions out
'''
# buildAllSubsets(4)
# generateAllFullSets(4)
# generateAllPermutations(4)
nQueens(5)
