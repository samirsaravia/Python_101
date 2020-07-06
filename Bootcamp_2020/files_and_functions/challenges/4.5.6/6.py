"""
Question 6
Write a function that will copy the contents of one file to a new file.
"""


def copy_file(infile, outfile):
    with open(infile) as file:
        with open(outfile, 'w') as new_file:
            new_file.write(file.read())


copy_file('capitals.txt', 'new_capitals.txt')
