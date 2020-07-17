import matplotlib.pyplot as plb
text = 'Science continues to simplify human life with every new research. Today, due to the increasing all-round ' \
       'development of science, humans are appearing in every field of the world. WIth the help od science, humans' \
       ' have controlled everything available on earth. WIth teh help of science we can fly in high sky and breathe ' \
       'in deep water. Due to the increasing development os science, we have been able o reach from Moon to Mars.' \
       ' The recent Mangalyaan of India successfully reaching the orbit of Mars is an example of increasing progress' \
       ' in human science. Things used to be impossible in ancient times. Due to the increasing use of science,' \
       ' she now feels ordinary. Due to new research in science, human gets rid of a new problem every day. ' \
       '20 years ago where malaria used to be considered a fatal disease now with the advancement of' \
       ' science, malaria has become a common disease. Science has made a lot fo progress in the medical system.' \
       ' Scientists have also slowly started catching hold of AIDS, which is considered incurable since last year. ' \
       'It is believed that due to the new medical system, the grip of AIDS is now weakening.' \
       ' And it is believed that in the near future this deadly disease will be eradicated from its roots.' \
       ' Today science is progressing double and night in the field of traffic. Where before it used t' \
       'o take days to go from one place to another. Now, in the era of airplanes and high speed trains,' \
       ' it can be reached from one place to another. Where earlier it was just a dream for the common people' \
       ' to travel by air fro higher fares. Today, with the changing times, common people are also able to afford' \
       ' the fare o air travel and enjoy air travel. In the last ten years, cars have reached almost every house' \
       ' in India, which directly explains the progress of science. a world of news is available on one click on online' \
       ' newspapers, online news sites, in this era of globalization, we know the news of the world by the press' \
       ' of a button on our mobile With Facebook, Twitter WhatsApp, no matter how far we are from our immediate' \
       ' relatives. But now through akk this we can stay connected with them for 24 hours. ' \
       'Thus new innovations of science are creating miracles in our life every day. Every day we are introduced' \
       ' o a new discovery, a new product which is simplifying the complexity of our lives'
data_index = dict()
for char in text.lower():
    data_index[char] = data_index.get(char, 0) + 1
data_index = {k: v for k, v in data_index.items() if k.isalpha()}
x, y = zip(*data_index.items())
plb.bar(x, y)
plb.show()
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def shift(num):
    calc = num % len(alphabet)
    return calc


def encrypt(text_input, num=0):
    encrypted_message = ''
    for char_input in text_input.lower():
        look_for = alphabet.find(char_input)
        if char_input not in alphabet:
            encrypted_message += char_input
        else:
            encrypted_message += alphabet[shift(look_for + num)]
    return encrypted_message


encrypt(text, 5)
