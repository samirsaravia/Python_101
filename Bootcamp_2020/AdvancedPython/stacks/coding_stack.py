"""
utf-8
    Coding a stack in Python
author: Samir S
"""


class Stack(object):
    def __init__(self):
        """
            Empty List
        """
        self.list_stack = []

    def is_empty(self):
        """
            To check it up
        :return: True if list is empty
        """
        if not self.list_stack:
            return True
        else:
            return False

    def push(self, item):
        """
            Adding elements to the list
        :param item: A int-digit appended to list_stack
        """
        self.list_stack.append(item)

    def pop(self):
        """
            Removing the last item of list_stack
        """
        self.list_stack.pop()

    def peek(self):
        """
            Checking the last item up
        :return: The last element of list if there is.
        """
        if not self.list_stack:
            return None
        else:
            return self.list_stack[-1]

    def __repr__(self):
        return repr(self.list_stack)


new_stack = Stack()
print(f'Is the stack empty? >>>> {new_stack.is_empty()}')
new_stack.push(45)
print(f'Picking the last item of the Stack >>> {new_stack.peek()}')
