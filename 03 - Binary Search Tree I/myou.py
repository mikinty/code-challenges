# BST I Solution
# Michael You

from Tree import Tree

def getClosest(T, N):
  if (T.right == None) and (T.left == None):
    return T # leaf or empty node
  else:
    currD = T.data - N # current distance
    if currD < 0: # need to search right
      comp = getClosest(T.right, N)
    else: # search left
      comp = getClosest(T.left, N)

    if comp != None and abs(currD) > abs(comp.data - N):
      return comp # recursed is closer
    else:
      return T # current one is closer

if __name__ == '__main__':
  # empty tree, should always return empty node
  T0 = Tree()

  for x in range(1000):
    assert(getClosest(T0, x).data == None)

  # singleton tree, should always return root node
  T1 = Tree()
  T1.data = 1

  for x in range(1000):
    res = getClosest(T1, (-x + 500)*30 + 34)
    assert(res.left == None)
    assert(res.right == None)
    assert(res.data == 1)

  # first nontrivial tree
  T2 = Tree()
  T2.data = 10
  T2.left = Tree()
  T2.left.data = 5
  T2.right = Tree()
  T2.right.data = 30
  T2.right.left = Tree()
  T2.right.left.data = 20
  T2.right.right = Tree()
  T2.right.right.data = 31

  # test cases
  testValues = [
    -17583,
    0,
    5,
    9,
    10,
    11,
    15,
    20,
    21,
    30,
    31,
    101203
  ]

  # the nodes that should be returned
  ans = [
    T2.left,
    T2.left,
    T2.left,
    T2,
    T2,
    T2,
    T2,
    T2.right.left,
    T2.right.left,
    T2.right,
    T2.right.right, 
    T2.right.right
  ]


  for x in range(len(testValues)):
    assert(getClosest(T2, testValues[x]) == ans[x])