import string

def rotate(text, key):
    result = []
    for letter in text:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            result.append(chr((ord(letter) - base + key) % 26 + base))
        else: result.append(letter)
    return ''.join(result)