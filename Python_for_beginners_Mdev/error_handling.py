x = 42
y = 0
print()
try:
    print(x / y)
except ZeroDivisionError as identifier:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong!')
finally:
    print('This is our cleanup!')
print()
'''
 when an exception occurs in the 'try' suite, a search for an exception handler is started.
This search inspects the except clauses in turn until one is found that matches the exception.
For an except clause with an expression , that expression is evaluated, and the clause matches the exception if the
resulting object is 'compatible' with the exception.
The optional 'else' is executed if the control flow leaves the 'try' suite, no exception was raised, and no 'return',
'continue', or 'break' statement was executed. Exceptions in the 'else clause are not handled by the preceding 'except'
clauses.
If 'finally' is present, it specifies a 'cleanup' handler.
'''
