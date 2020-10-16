from twilio.rest import Client

account_sid = 'AC8c216d087c75c5ebedff2002036beccc'
auth_token = '972f33bdc680ed1a9e991da4b2248bad'
client = Client(account_sid, auth_token)


def send_love():
    message = client.messages.create(from_='whatsapp:+14155238886',
                                     body='Hummm?',
                                     to='whatsapp:+5516994083055')

    print(message.sid)
