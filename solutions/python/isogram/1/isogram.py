import string

def is_isogram(phrase):
    sentence = [c for c in phrase.lower() if c.isalpha()]
    return len(sentence) == len(set(sentence))
