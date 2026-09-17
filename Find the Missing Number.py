def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for value in numbers:
        actual_sum += value

    return expected_sum - actual_sum


n = int(input())
numbers = list(map(int, input().split()))

print(find_missing_number(numbers, n))
