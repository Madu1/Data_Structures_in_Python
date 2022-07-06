# by using inbuilt class which is deque
from collections import deque


#
# stack = deque()
# stack.append('https://edition.cnn.com/asia')
# stack.append('https://edition.cnn.com/')
# stack.append('https://edition.cnn.com/australia')
#
# print(stack)
# print(stack.pop())
# print(stack)

# let's implement Stack class
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    # return the reverse string
    def reverse_str(self, string):
        for i in range(0, len(string)):
            self.push(string[i])
        reverse_str = ' '
        for j in range(0, len(string)):
            reverse_str += self.pop()
        return reverse_str

    @staticmethod
    def is_match(ch1, ch2):
        match_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        return match_dict[ch1] == ch2

    @staticmethod
    def is_balanced(s):
        stack = Stack()
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.push(ch)
            if ch == ')' or ch == '}' or ch == ']':
                if stack.size() == 0:
                    return False
                if not Stack.is_match(ch, stack.pop()):
                    return False

        return stack.size() == 0


stk = Stack()
# s.push('https://edition.cnn.com/asia')
# s.push('https://edition.cnn.com/')
# s.push('https://edition.cnn.com/australia')
# print(s.peek())
# print(s.pop())
# print(s.size())

# string = 'We will conquere COVID-19'
# print(stk.reverse_str(string))
print(Stack.is_balanced("({a+b})"))
print(Stack.is_balanced('))((a+b}{'))
print(Stack.is_balanced('((a+b))'))
print(Stack.is_balanced('((a+g))'))
print(Stack.is_balanced('))'))
print(Stack.is_balanced('[a+b]*(x+2y)*{gg+kk}'))