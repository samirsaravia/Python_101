import re

#
# [aeiou] Match any vowel
# [^aeiou] ^ inverts selection, this matches any consonant
# [a-z] Match any lowercase letter from a-z
# \d Matches any decimal digit; this is equivalent to the class [0-9]
# \D Matches any non-digit character; this is equivalent to the class
# [^0-9]
# \s Matches any whitespace character; this is equivalent to the
# class [ \t\n\r\f\v]
# \S Matches any non-whitespace character; this is equivalent to the
# class [^ \t\n\r\f\v]
# \w Matches any alphanumeric character; this is equivalent to the
# class [a-zA-Z0-9_]
# \W Matches any non-alphanumeric character; this is equivalent to
# the class [^a-zA-Z0-9_]


# set a pattern using re module
pattern = re.compile(r'samir')
print(pattern.match('samir'))

# Match expressions to the pattern
me = pattern.match('samir')
print(me.group())

me_2 = pattern.match('hello samir')

me_3 = pattern.search('hello samir')
print(me_3)
print(me_3.group())

pattern_2 = re.compile(r's\D+')
print(pattern_2.match('samir12345'))

# searching for specific data
string = '''image01.jpg,image01.png,image02.jpg,my_doc.doc,my_doc2.docx,
london_bridge.gif, another_doc.doc,my_pdf.pdf'''
pattern_3 = re.compile(r'(\w+)\.(jpg|png|gif)')
print(pattern_3)

for m in re.finditer(pattern_3, string):
    print(m.group())
