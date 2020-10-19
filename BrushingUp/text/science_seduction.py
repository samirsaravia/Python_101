import matplotlib.pyplot as plt

text = 'Sherlock Holmes took his bottle from the corner of the mantel-piece ' \
       'and his hypodermic syringe from its neat morocco case. With his ' \
       'long, white, nervous fingers he adjusted the delicate needle, ' \
       'and rolled back his left shirt-cuff. For some little time his eyes ' \
       'rested thoughtfully upon the sinewy forearm and wrist all dotted and '\
       'scarrred with innumerablle puncture-marks Finally' \
       'he thrust the sharp point home, pressed down the tiny piston home, ' \
       'the velvet-lined arm-chair with a long sigh of satisfaction.' \
       'Three times a day from many months I had witnessed this performance, '\
       'but had witnessed' \
       'this performance, but custom had not reconciled my mind to it. On ' \
       'the contrary , from day to day I had become more irritable at the ' \
       'sight, and my conscience swelled nightly within me at the thought ' \
       'that I had lacked the courage to protest. Again and again I had ' \
       'registered a vow that I should deliver m soul upon the subject, ' \
       'but there was that in the cool, nonchalant air of my comapnion which '\
       'made' \
       'him the last man with whom on ewould care to take anything ' \
       'approaching to a liberty. HIs great powers, his mastery manner, ' \
       'and great powers, his masterly manner, and the experienc which I had '\
       'of his many extraordinary qualities all made me dififident and ' \
       'backward in crossing him. Yet upon that afternoon, whether it was ' \
       'Beaune which I had taken with my lunch, or the additional ' \
       'exasperation produced  by the exreme deliberation of his manner, ' \
       'I suddenly felt that I could hold out no longer." which is to-day" I '\
       'asked' \
       '"morphine or cocaine" He raised his eyes languidly from the old ' \
       'black-letter volume whcih he had opened. It is cocaine he said, ' \
       'a seven-per-cent solution. Would you care to try it.' \
       'No, indeed, I answered, brusquely. My consittution has not got over ' \
       'the Afghan campaing yet. I cannot afford to throw any extra strain ' \
       'upon it. He smiled at my vehemence. Perhaps you are right, Watson, ' \
       'he said. I suppose that its influence is physicaly a bad one. I find '\
       'it, however, so transcendentaly stimulating and clarigying to the ' \
       'mind ath its secondary actioin is a matter of small moment. '

char = dict()
for i in text.lower():
    char[i] = char.get(i, 0) + 1

just_letter = {lett: qua for lett, qua in char.items() if lett.isalpha()}
x, y = zip(*just_letter.items())
plt.bar(x, y)
plt.show()


def shift(number: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    calculate = number % len(alphabet)
    return calculate


def encrypt(txt: str, code: int = 0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for ch in txt.lower():
        check = alphabet.find(ch)
        if ch not in alphabet:
            encrypted += ch
        else:
            encrypted += alphabet[shift(check + code)]
    return encrypted


print(encrypt(text, 35))
