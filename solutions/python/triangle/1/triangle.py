

def equilateral(sides):
    tri = sorted(sides)
    if all(side > 0 for side in sides) and tri[0] + tri[1] >= tri[2]:
        return len(set(sides)) == 1
    return False

def isosceles(sides):
    tri = sorted(sides)
    if all(side > 0 for side in sides) and tri[0] + tri[1] >= tri[2]:
        return len(set(sides)) <= 2
    return False
    

def scalene(sides):
    tri = sorted(sides)
    if all(side > 0 for side in sides) and tri[0] + tri[1] >= tri[2]:
        return len(set(sides)) == 3
    return False
