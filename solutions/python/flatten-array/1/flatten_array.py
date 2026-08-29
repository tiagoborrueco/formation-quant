def flatten(iterable):
    résultat = []
    for item in iterable:
        if isinstance(item, list):
            sous_résultat = flatten(item)
            résultat = [*résultat, *sous_résultat]
        elif item != None:
            résultat.append(item)
    return résultat
    
