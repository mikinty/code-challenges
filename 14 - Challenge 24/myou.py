class Solution:
    def judgeCardsNoPrint(self, cards):
        if len(cards) == 0:
            return False  # this should never be the case
        elif len(cards) == 1:
            return abs(cards[0] - 24) < 1e-9
        else:
            # try all combinations (choose) of two numbers in the cards,
            # calculate all possible values they can have, and recurse on them
            # plus the remaining nucards
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    a = cards[i]
                    b = cards[j]

                    rem_numbers = [cards[x] for x in range(
                        len(cards)) if (x != i and x != j)]

                    possible = set([a-b, b-a, a*b, a+b])

                    if a != 0:
                        possible.add(b/a)
                    if b != 0:
                        possible.add(a/b)

                    for val in possible:
                        if self.judgeCardsNoPrint(rem_numbers + [val]):
                            return True

            return False

    def judgeCards(self, cards, currExp={}, possibleExpr=''):
        if len(cards) == 0:
            return False  # this should never be the case
        elif len(cards) == 1:
            res = abs(cards[0] - 24) < 1e-9
            if res:
                print(possibleExpr[cards[0]])
            return res
        else:
            # try all combinations of two numbers in the cards, and recurse on them
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    a = cards[i]
                    b = cards[j]

                    rem_numbers = [cards[x] for x in range(
                        len(cards)) if (x != i and x != j)]

                    possible = set([a-b, b-a, a*b, a+b])
                    possibleExpr = {}
                    if a in currExp:
                        aExp = currExp[a]
                    else:
                        aExp = f'{a}'

                    if b in currExp:
                        bExp = currExp[b]
                    else:
                        bExp = f'{b}'

                    possibleExpr[a-b] = f'({aExp}-{bExp})'
                    possibleExpr[b-a] = f'({bExp}-{aExp})'
                    possibleExpr[a*b] = f'{aExp}*{bExp}'
                    possibleExpr[a+b] = f'({aExp}+{bExp})'

                    if a != 0:
                        possible.add(b/a)
                        possibleExpr[b/a] = f'{bExp}/{aExp}'
                    if b != 0:
                        possible.add(a/b)
                        possibleExpr[a/b] = f'{aExp}/{bExp}'

                    for val in possible:
                        currExp[val] = possibleExpr[val]
                        if self.judgeCards(rem_numbers + [val], currExp, possibleExpr):
                            return True

                        try:
                            del currExp[val]
                        except:
                            print('deleting', val, 'from', currExp)

            return False

    def judgePoint24(self, cards):
        return self.judgeCardsNoPrint(cards)


sol = Solution()
print(sol.judgePoint24([8, 3, 8, 3]))
print(sol.judgePoint24([8, 3, 1, 1]))
print(sol.judgePoint24([1, 4, 5, 6]))
print(sol.judgePoint24([100, 3, 54, 7]))
