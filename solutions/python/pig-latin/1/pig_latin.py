def translate(sentence):
    words = sentence.split()
    for text in words:
        if text[0] in "aeiou" or text[0:2] == "xr" or text[0:2] == "yt" or text[0:2] == "ay":
            translation = text + "ay"

        if text[0] in "bcdfghjklmnpqrstvwxyz" and not (text[0:2] == "xr" or text[0:2] == "yt" or text[0:2] == "ay"):
            cons_number = 0
            while text[cons_number] in "bcdfghjklmnpqrstvwxyz":
                if (cons_number >= 1 and text[cons_number] == "y"):
                    break
                cons_number = cons_number + 1
            translation = text[cons_number:] + text[:cons_number] + "ay"
        if translation[0] == "u" and translation[-3] == "q":
            translation = translation[1:-2] + "u" + translation[-2:]

        words[words.index(text)] = translation

    answer = " ".join(words)
    return answer


























    
