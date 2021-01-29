# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
from packages.api.password import Password

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACbba09c3524af4229668efec0ed7ea4a3", "6395102521c45483db065cba259a0e99")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
def sendSms():
    code = Password().get_random_sms_password()
    if client.messages.create(to="+33781571629",
                           from_="+14124192839",
                           body=f"\n Voici ton code connexion: {code}"):
        print("envoyé")
        return code