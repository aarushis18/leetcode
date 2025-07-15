class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        running = []

        for token in tokens:

            if token == '+':
                first = int(running.pop())
                second = int(running.pop())
                running.append(int(first + second))

            elif token == '-':
                first = int(running.pop())
                second = int(running.pop())
                running.append(int(second - first))

            elif token == '*':
                first = int(running.pop())
                second = int(running.pop())
                running.append(int(first * second))

            elif token == '/':
                first = int(running.pop())
                second = int(running.pop())
                running.append(int(second / first))

            else:               # assuming we have a number, otherwise we would be error checking
                running.append(int(token))

        return running[-1]