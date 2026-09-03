def find_largest(numbers):
    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


n = int(input())
numbers = list(map(int, input().split()))

print(find_largest(numbers))
