import random
import string
import urllib.parse # For URL encoding

class PassGenerate:
    def __init__(self, length=16):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self):
        if self.length < 4:
            raise ValueError("Password length should be at least 4 to include all character types.")

        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        password += random.choices(self.characters, k=self.length - 4)
        random.shuffle(password)  # Shuffle to ensure randomness
        return ''.join(password)

    def set_length(self, length):
        if length < 4:
            raise ValueError("Password length should be at least 4.")
        self.length = length

    def generate_encoded_password(self):
        password = self.generate()
        encoded_password = urllib.parse.quote(password)
        return encoded_password
