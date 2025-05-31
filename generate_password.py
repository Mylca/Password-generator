import secrets
import string


def generate_mandatory_chars(digit, lower, upper, special):
    mandatory_chars = []

    if digit:
        mandatory_chars.append(secrets.choice(string.digits))
    if lower:
        mandatory_chars.append(secrets.choice(string.ascii_lowercase))
    if upper:
        mandatory_chars.append(secrets.choice(string.ascii_uppercase))
    if special:
        mandatory_chars.append(secrets.choice(string.punctuation))

    return mandatory_chars


def remaining_chars(length, characters):
    return [secrets.choice(characters) for i in range(length)]


def shuffle_password(password):
    secrets.SystemRandom().shuffle(password)
    return None


def generate_password(length=16, upper=True, lower=True,
                      digit= True, special=True):
    mandatory_chars = generate_mandatory_chars(upper, lower, digit, special)

    remaining_length = length - len(mandatory_chars)

    characters = string.ascii_lowercase
    if upper:
        characters += string.ascii_uppercase
    if digit:
        characters += string.digits
    if special:
        characters += string.punctuation

    password = mandatory_chars + remaining_chars(remaining_length, characters)

    shuffle_password(password)

    return ''.join(password)

if __name__ == '__main__':
    generate_password()
