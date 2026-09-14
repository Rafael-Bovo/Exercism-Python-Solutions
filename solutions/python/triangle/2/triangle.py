def triangle_condition(sides: int):
    
    '''
    Parameters:
    sides: a list of possible sides of a tringle

    Input: 
    The possible sides of a triangle

    Output:
    If the sides caracterize a triangle or not (bool)
    '''
    
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    
    if sides[0] <= sides[1] + sides[2]:
        if sides[1] <= sides[0] + sides[2]:
            if sides[2] <= sides[0] + sides[1]:
                return True

    return False



def equilateral(sides: int):
    
    '''
    Parameters:
    sides: a list of possible sides of a tringle

    Input: 
    The possible sides of a triangle

    Output:
    If the sides caracterize a equilateral triangle or not (bool)
    '''
    
    if triangle_condition(sides) and sides[0] == sides[1] and sides[1] == sides [2]:
        return True
        
    return False


def isosceles(sides: int):
    
    '''
    Parameters:
    sides: a list of possible sides of a tringle

    Input: 
    The possible sides of a triangle

    Output:
    If the sides caracterize a isoceles triangle or not (bool)
    '''
    
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
    
    '''
    Parameters:
    sides: a list of possible sides of a tringle

    Input: 
    The possible sides of a triangle

    Output:
    If the sides caracterize a scalene triangle or not (bool)
    '''
    
    if triangle_condition(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True

    return False
