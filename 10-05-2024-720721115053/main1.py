def Number(numbers):
    result = 0
    for number in numbers:
        result ^= number
    return result
print("Use Case 1")
print(Number([2, 2, 1]))
print("Use Case 2")
print(Number([4, 1, 2, 1, 2]))
print("Use Case 3")
print(Number([1]))