def append(list1, list2):
    app = [*list1, *list2]
    return app


def concat(lists):
    con = []
    for item in lists:
        con = [*con , *item]
    return con
        


def filter(function, list):
    fil = []
    for item in list:
        if function(item):
            fil.append(item)
    return fil
        


def length(list):
    return len(list)


def map(function, list):
    map = []
    for item in list:
        map.append(function(item))
    return map


def foldl(function, list, initial):
    accumulateur = initial
    for item in list:
        accumulateur = function(accumulateur, item)
    return accumulateur


def foldr(function, list, initial):
    accumulateur = initial
    for item in reversed(list):
        accumulateur = function(accumulateur, item)
    return accumulateur


def reverse(liste):
    new = list(reversed(liste))
    return new
