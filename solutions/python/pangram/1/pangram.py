import string

def is_pangram(sentence):
    sentence = set(sentence.lower())
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(sentence)
