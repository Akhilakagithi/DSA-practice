def arrange_elements(numbers):
    j = 0

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1

    return numbers
