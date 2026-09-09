def rotate_right(numbers):
    if len(numbers) <= 1:  #if the array has 1 or 0 elements stop and go back
        return

    last = numbers[-1]

    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]

    numbers[0] = last


n = int(input())
numbers = list(map(int, input().split()))

rotate_right(numbers)
print(*numbers)
