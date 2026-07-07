def find_anagrams(word, candidates):
    result = []
    for candidate in candidates:
        if (len(word) == len(candidate)
        and word.lower() != candidate.lower()
        and sorted(word.lower()) == sorted(candidate.lower())):
            result.append(candidate)
    return result

