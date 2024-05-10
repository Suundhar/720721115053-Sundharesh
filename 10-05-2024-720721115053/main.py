def staircase(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
print("Use Case 1")
print(staircase(2))
print("Use Case 2")
print(staircase(3))