import secrets
import string


class Password:
    def __init__(self):
        super().__init__()
        self.default_key_lenght = 20

    def get_random_password(self):
        random_source = string.ascii_letters + string.digits + string.punctuation
        password = secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.digits)
        password += secrets.choice(string.punctuation)

        for i in range(10):
            password += secrets.choice(random_source)

        password_list = list(password)
        secrets.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)

        return password

    def get_random_key(self, length):
        key_characters = string.ascii_letters + string.digits + string.punctuation
        key = ''.join(secrets.choice(key_characters) for i in range(length))

        return key

    def get_random_sms_password(self):
        digits = string.digits
        sms_key = ''.join(secrets.choice(digits) for i in range(6))

        return sms_key


if __name__ == '__main__':
    passWords = Password()
    myPassword = passWords.get_random_password()
    myKey = passWords.get_random_key(20)
    mySmsPass = passWords.get_random_sms_password()

    print(f"Voici ton mdp: {myPassword}")
    print(f"Voici ta clé de connexion: {myKey}")
    print(f"Voici ta clé de connexion sms: {mySmsPass}")