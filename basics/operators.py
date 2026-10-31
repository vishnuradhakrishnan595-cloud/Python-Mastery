"""Arithmetic, comparison, logical, membership, and assignment operators."""


def main():
    a = 10
    b = 3

    print("Arithmetic")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a // b =", a // b)
    print("a % b =", a % b)
    print("a ** b =", a ** b)

    print("\nComparison")
    print("a > b:", a > b)
    print("a == b:", a == b)
    print("a != b:", a != b)

    print("\nLogical")
    print("a > 5 and b < 5:", a > 5 and b < 5)
    print("a < 5 or b < 5:", a < 5 or b < 5)
    print("not (a == b):", not (a == b))

    print("\nMembership")
    print("'py' in 'python':", "py" in "python")

    a += 2
    print("\nAfter a += 2:", a)


if __name__ == "__main__":
    main()
