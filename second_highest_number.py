def find_second_highest(numbers):
    largest = None
    second_highest = None

    for number in numbers:

        if largest is None or number > largest:
            second_highest = largest
            largest = number

        elif number != largest:
            if second_highest is None or number > second_highest:
                second_highest = number

    return second_highest
