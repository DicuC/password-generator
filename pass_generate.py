import random
import string

class PassGenerate:
    def __init__(self, length=16):  # Default length set to 16
        self.length = length
        self.characters = string.ascii_letters + string.digits

    def generate(self):
        if self.length < 4:
            raise ValueError("Password length should be at least 4 to include all character types.")
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits)
        ]
        password += random.choices(self.characters, k=self.length - 3)
        random.shuffle(password)
        return ''.join(password)

    def set_length(self, length):
        if length < 4:
            raise ValueError("Password length should be at least 4.")
        self.length = length