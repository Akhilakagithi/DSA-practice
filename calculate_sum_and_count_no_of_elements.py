def calculate_sum_and_count(numbers):
    total = 0
    count = 0

    for i in numbers:
        total += i
        count += 1

    return total, count
n = int(input())
numbers = list(map(int, input().split()))
