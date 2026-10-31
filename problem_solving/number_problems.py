"""Common number problems with validation and example calls."""


def even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is defined here only for non-negative integers.")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def fibonacci(count: int) -> list[int]:
    if count < 0:
        raise ValueError("Count cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_armstrong(number: int) -> bool:
    """Check whether a non-negative integer equals the sum of its digits to a power."""
    if number < 0:
        return False
    digits = [int(char) for char in str(number)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == number


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor using Euclid's algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def main():
    print("10 is", even_or_odd(10))
    print("29 is prime:", is_prime(29))
    print("5! =", factorial(5))
    print("First 8 Fibonacci numbers:", fibonacci(8))
    print("153 is Armstrong:", is_armstrong(153))
    print("GCD of 48 and 18:", gcd(48, 18))


if __name__ == "__main__":
    main()
