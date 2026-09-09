def move_zeros(numbers):
    j = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1


n = int(input())
numbers = list(map(int, input().split()))

move_zeros(numbers)

print(*numbers)
