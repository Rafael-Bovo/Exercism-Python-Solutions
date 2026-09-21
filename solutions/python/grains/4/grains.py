def board_check(number: int):
    '''
    Function to get if the input square is valid
    
    input: 
        number: square's value

    output(type:bool) : return if is true the fuction
    '''
    
    if 1 <= number <= 64:
        return True
    return False
        


def square(number: int):
    '''
    Function to calculate the value of the desired square

    input:
        number: square's value

    output(type:int): return the square value
    
    exception message: return if the square is off the designed range (1 <= square value <= 64)
    '''

    
    if board_check(number):
        square_value = 2 ** (number - 1)
        return square_value

    if not board_check(number):
        raise ValueError("square must be between 1 and 64")

    return None
    


def total():
    '''
    Function to calculate the value of the last square in the board (number 64)
    
    output(type: int): return the max value
    '''
    
    MAX_SQUARE = 64
    total_number = 2 ** MAX_SQUARE - 1
    
    return total_number
