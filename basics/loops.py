"""for loops, while loops, range, break, and continue."""


def main():
    print("Numbers from 1 to 5:")
    for number in range(1, 6):
        print(number)

    print("\nEven numbers below 10:")
    for number in range(10):
        if number % 2 != 0:
            continue
        print(number)

    print("\nStop when number reaches 4:")
    for number in range(1, 8):
        if number == 4:
            break
        print(number)

    print("\nCountdown:")
    count = 3
    while count > 0:
        print(count)
        count -= 1
    print("Go!")

    print("\nMultiplication table for 3:")
    for multiplier in range(1, 11):
        print(f"3 x {multiplier} = {3 * multiplier}")


if __name__ == "__main__":
    main()
