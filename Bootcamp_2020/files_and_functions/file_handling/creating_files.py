"""
File handling in Python
Python can open, close, read and write to files
"""
f = open('kipling.txt', 'w')
f.write('If you can trust yourself when all men doubt you ,\n\
but make allowance for their doubting too.\n')

f.write('If you can wait and not be tired by waiting ,\n\
Or being lied about you, don\'t deal in lies.\n')
f.write('Or being hated, don\'t give way to hating,\n\
don\'t look too good nor talk too wise.\n')
f.close()
