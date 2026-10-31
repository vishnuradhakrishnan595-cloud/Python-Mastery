"""List creation, indexing, slicing, updates, and common operations."""


def main():
    numbers = [10, 20, 30]
    print("Original:", numbers)

    numbers.append(40)
    numbers.extend([50, 60])
    numbers.insert(0, 5)
    print("After adding:", numbers)

    numbers.remove(20)
    removed = numbers.pop()
    print("Removed last value:", removed)
    print("After removals:", numbers)

    print("First:", numbers[0])
    print("Last:", numbers[-1])
    print("Slice:", numbers[1:4])
    print("Length:", len(numbers))

    numbers.sort()
    print("Sorted:", numbers)
    print("Reversed copy:", numbers[::-1])

    squares = [value * value for value in range(1, 6)]
    print("Squares:", squares)

    odds = [value for value in range(1, 11) if value % 2 != 0]
    print("Odds from 1 to 10:", odds)


if __name__ == "__main__":
    main()
