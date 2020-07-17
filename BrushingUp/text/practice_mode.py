from collections import Counter
import matplotlib.pyplot as pyp
text = "We can look upon a road from who different points of view. One regards it as dividing us from the object of our " \
       "desire; in that case we count every step of our journey over it as something attained by force n the face " \
       "of obstruction. The other sees it as the road which leads us to our destination: and as such it is part of our " \
       "goal. It is already the beginning of our attainment, and by journeying over it we can only gain that whcih in" \
       " itself it offers to us. This last point of view is that of India with regard to nature. For her, the great" \
       " fact is that we are in harmony with nature; that man can think because his thoughts are in harmony with things " \
       "that he can use the fores of nature for his own purpose only because his universal, and that in the ong " \
       "run his purpose never can knock against the purpose which works through nature. In the west the prevalent " \
       "feeling is that nature belongs exclusively to inanimate thigns and to beasts, that there is a sudden " \
       "unaccountable break where human-nature begins. According t it, everyting that is low in the scale of " \
       "beings is merely nature, and whatever has the stamp of perfection on it, intellecutal or moral, " \
       "is human-nature. It is like dividing the bud and putting their grace to the credit of two" \
       " different and antithetical principles. But ehe Indian mind never has any hesitation in acknowledging " \
       "its kinship with nature, its unbroken relation with all. "

letter_count = dict(Counter(text.lower()))
letter_count = {k: v for k, v in letter_count.items() if k.isalpha()}

x, y = zip(*letter_count.items())
pyp.bar(x, y)
pyp.show()
