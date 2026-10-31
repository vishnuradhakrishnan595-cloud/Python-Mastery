"""Sets store unique hashable values and support set operations."""


def main():
    numbers = {1, 2, 2, 3, 3, 3}
    print("Duplicates removed:", numbers)

    first = {1, 2, 3, 4}
    second = {3, 4, 5, 6}

    print("Union:", first | second)
    print("Intersection:", first & second)
    print("Difference:", first - second)
    print("Symmetric difference:", first ^ second)

    first.add(7)
    first.discard(100)  # Does not fail if 100 is absent.
    print("Updated set:", first)

    names = ["Ana", "Ben", "Ana", "Cara", "Ben"]
    unique_names = set(names)
    print("Unique names:", sorted(unique_names))


if __name__ == "__main__":
    main()
