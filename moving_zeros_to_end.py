def move_zeroes(numbers):
    position = 0

    
    for number in numbers:
        if number != 0:
            numbers[position] = number
            position += 1

    
    while position < len(numbers):
        numbers[position] = 0
        position += 1

    return numbers
