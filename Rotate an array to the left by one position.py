def rotate_left(numbers):
    if len(numbers) <= 1:
        return numbers

    first = numbers[0]

    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i + 1]

    numbers[-1] = first

    return numbers


n = int(input())
numbers = list(map(int, input().split()))

rotate_left(numbers)

print(*numbers)
