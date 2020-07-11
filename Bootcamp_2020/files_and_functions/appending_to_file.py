f = open('kipling.txt', 'w')
f.write('If you can trust yourself when all men doubt you ,\n\
but make allowance for their doubting too.\n')

f.write('If you can wait and not be tired by waiting ,\n\
Or being lied about you, don\'t deal in lies.\n')
f.write('Or being hated, don\'t give way to hating,\n\
don\'t look too good nor talk too wise.\n')
f.close()

# f = open('kipling.txt', 'a')
# f.write('If you can dream -  and not make dreams your master \n\
# If you can think and not make thoughts your aim\n')
# f.close()
# f = open('kipling.txt', 'r')
# print(f.read())
# f.close()

# better way reading a file without worrying about to close it.
with open('kipling.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')
