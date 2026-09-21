def board_check(number: int):
    if 1 <= number <= 64:
        return True
    return False
        


def square(number: int):
    if board_check(number):
        square_value = 2 ** (number - 1)
        return square_value

    if not board_check(number):
        raise ValueError("square must be between 1 and 64")
        
    


def total():
    MAX_SQUARE = 64
    total_number = 2 ** MAX_SQUARE - 1
    
    return total_number
