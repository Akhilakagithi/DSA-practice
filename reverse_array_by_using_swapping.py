def reverse_array(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1


n = int(input())
numbers = list(map(int, input().split()))

reverse_array(numbers)
print(*numbers)
