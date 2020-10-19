"""
Mad libs is some kind of program where you create a story with a number of
words missing - you could also use a pre-built template for the same. You
then have to work out the part of speech - whether adjective, noun, adverb,
and so on--
"""
name = input('Name a noun: ')
verb_past = input('Name a past tense verb: ')
adjective = input('Name an adjective: ')
animal_pl = input('Name an animal in plural: ')
prof = input('Name a profession: ')

print("%s Dumpty %s on wall.%s Dumpty had an %s fall.\n"
      "All the king's %s "
      "and the %s's men\n"
      "Could not put %s together again" % (name, verb_past, name,
                                           adjective, animal_pl, prof, name))
