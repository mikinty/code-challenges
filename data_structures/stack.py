'''
Implementation of a stack

Author: mikinty
'''

from enum import Enum, auto


class StackInstruction(Enum):
    '''
    Set of instructions used in the Stack class
    '''
    PUSH = auto()
    POP = auto()
    TOP = auto()


class Stack:
    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, element):
        '''
        Adds an element to the top of the stack
        O(1)
        '''
        self.stack.append(element)
        self.history.append(
            {'instruction': StackInstruction.PUSH, 'element': element})

    def pop(self):
        '''
        Removes the topmost element from the stack
        O(1)
        '''
        if len(self.stack) <= 0:
            self.history.append(
                {'instruction': StackInstruction.POP, 'error': 'Tried to pop from an empty stack'})
            return None

        element = self.stack.pop()
        self.history.append(
            {'instruction': StackInstruction.POP, 'element': element})
        return element

    def top(self):
        '''
        Returns the top element on the stack, without removing it from the stack
        O(1)
        '''
        if len(self.stack) <= 0:
            self.history.append(
                {'instruction': StackInstruction.TOP, 'error': 'Tried to view the top of an empty stack'})
            return None

        return self.stack[-1]

    def show(self):
        '''
        Prints out the entire stack
        O(n)
        '''
        print(self.stack)

    def showHistory(self, recent=10):
        '''
        Prints out the history of the stack, limited to the most recent ones
        O(n_i) where n_i is the number of operations run by the stack
        '''
        historySegment = self.history[max(-1-recent, -1-len(self.history)): -1]

        for i in range(len(historySegment)):
            print(historySegment[i])


stack = Stack()

stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
print('TOP', stack.top())
stack.show()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print('TOP', stack.top())
stack.showHistory()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.showHistory()
