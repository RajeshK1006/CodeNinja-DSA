def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    r = 0
        
    for i in range(1, n + 1):
        divisor_sum = 0
        sqrt_i = int(i**0.5) + 1
        for j in range(1, sqrt_i):
            if i % j == 0:
                divisor_sum += j
                if j != i // j:  # Avoid adding twice for perfect squares
                    divisor_sum += i // j
        r += divisor_sum
    return r