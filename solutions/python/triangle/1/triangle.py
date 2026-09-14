def triangle_condition(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    
    if (sides[0] <= sides[1] + sides[2]):
        if (sides[1] <= sides[0] + sides[2]):
            if (sides[2] <= sides[0] + sides[1]):
                return True

    return False



def equilateral(sides):
    if triangle_condition(sides) and sides[0] == sides[1] and sides[1] == sides [2]:
        return True
        
    return False


def isosceles(sides):
    if triangle_condition(sides) and sides[0] == sides[1] and sides[1] != sides[2]:
        return True
    if triangle_condition(sides) and sides[1] == sides[2] and sides[0] != sides[1]:
        return True
    if triangle_condition(sides) and sides[0] == sides[2] and sides[0] != sides[1]:
        return True
    if triangle_condition(sides) and sides[0] == sides[1] and sides[1] == sides [2]:
        return True
        
    return False


def scalene(sides):
    if triangle_condition(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True

    return False
