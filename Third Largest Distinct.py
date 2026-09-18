def third_largest_distinct(numbers):
    first = None
    second = None
    third = None

    for value in numbers:

        # Skip duplicates
        if value == first or value == second or value == third:
            continue

        # Find largest
        if first is None or value > first:
            third = second
            second = first
            first = value

        # Find second largest
        elif second is None or value > second:
            third = second
            second = value

        # Find third largest
        elif third is None or value > third:
            third = value

    if third is None:
        return -1

    return third
