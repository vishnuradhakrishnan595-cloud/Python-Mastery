"""List challenges: filtering, searching, duplicates, and two-sum."""


def remove_evens(numbers: list[int]) -> list[int]:
    """Return a new list containing only odd values."""
    return [number for number in numbers if number % 2 != 0]


def second_largest(numbers: list[int]) -> int:
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        raise ValueError("At least two distinct values are required.")
    return unique_numbers[1]


def find_duplicates(numbers: list[int]) -> list[int]:
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return sorted(duplicates)


def linear_search(numbers: list[int], target: int) -> int:
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


def two_sum(numbers: list[int], target: int) -> list[int] | None:
    """Return indices of two values that add to target, or None."""
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        seen[number] = index
    return None


def rotate_right(numbers: list[int], steps: int) -> list[int]:
    if not numbers:
        return []
    steps %= len(numbers)
    if steps == 0:
        return numbers[:]
    return numbers[-steps:] + numbers[:-steps]


def main():
    values = [8, 3, 6, 3, 9, 2, 8]
    print("Odd values:", remove_evens(values))
    print("Second largest distinct:", second_largest(values))
    print("Duplicates:", find_duplicates(values))
    print("Index of 9:", linear_search(values, 9))
    print("Two-sum indices:", two_sum([2, 7, 11, 15], 9))
    print("Rotate right:", rotate_right([1, 2, 3, 4, 5], 2))


if __name__ == "__main__":
    main()
