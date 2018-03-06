"""
Evaluate RPN expressions
Write a program that takes an TPN and returns the number that
the expression evaluates to

Let's assume it's given as an array of strings
A = ['1', '2', '+']
Would return 3 (1+2)
How to implement with a stack?
Pop the expression
Pop the next two values
Exaluate expression
"""


class StackWithMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty:
            raise Exception('underflow')
        else:
            return self.items.pop()

    def get_max(self):
        return max(self.items)


def rpn_calculator(A):
    intermediate_results = []
    for token in A:
        if token == '+':
            intermediate_results.append(intermediate_results.pop() +
                                        intermediate_results.pop())
        elif token == '-':
            intermediate_results.append(intermediate_results.pop() -
                                        intermediate_results.pop())
        elif token == '*':
            intermediate_results.append(intermediate_results.pop() *
                                        intermediate_results.pop())
        elif token == '/':
            intermediate_results.append(intermediate_results.pop() /
                                        intermediate_results.pop())
        else:
            intermediate_results.append(int(token))

    return intermediate_results.pop()

if __name__ == '__main__':
    A = ['3','4','+','2','*','1','+']
    print(rpn_calculator(A))

