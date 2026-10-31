"""Interview practice prompts with reference solutions.

Try each problem yourself before checking the function implementation.
"""


def fizzbuzz(limit: int) -> list[str]:
    if limit < 0:
        raise ValueError("Limit cannot be negative.")
    result = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result


def find_missing_number(numbers: list[int], n: int) -> int:
    """Find the missing value from 1..n, assuming exactly one is missing."""
    if n < 1:
        raise ValueError("n must be positive.")
    if len(numbers) != n - 1:
        raise ValueError("Input must contain exactly n - 1 values.")
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input values must be unique.")
    if any(number < 1 or number > n for number in numbers):
        raise ValueError("Values must be in the range 1..n.")
    expected = n * (n + 1) // 2
    return expected - sum(numbers)


def is_valid_brackets(text: str) -> bool:
    """Check whether (), [], and {} brackets are correctly balanced."""
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack = []
    for char in text:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def josephus_last_position(n: int, step: int = 2) -> int:
    """Return the 1-based survivor position for the Josephus counting rule."""
    if n < 1 or step < 1:
        raise ValueError("n and step must be positive.")
    survivor = 0
    for size in range(2, n + 1):
        survivor = (survivor + step) % size
    return survivor + 1


def main():
    print("FizzBuzz 1..15:", fizzbuzz(15))
    print("Missing number:", find_missing_number([1, 2, 4, 5], 5))
    print("Valid brackets:", is_valid_brackets("{[()]}"))
    print("Invalid brackets:", is_valid_brackets("{[(])}"))
    print("Josephus survivor for 7 people, step 2:", josephus_last_position(7, 2))


if __name__ == "__main__":
    main()
