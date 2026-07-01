def response(hey_bob):
    if hey_bob.strip().endswith('?') and not hey_bob.isupper():
        return 'Sure.'
    if hey_bob.isupper() and not hey_bob.endswith('?'):
        return "Whoa, chill out!"
    if hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if hey_bob == "" or not hey_bob.strip():
        return "Fine. Be that way!"
    return 'Whatever.'
