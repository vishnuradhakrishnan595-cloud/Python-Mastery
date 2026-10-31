"""Tuples: ordered, immutable collections."""


def main():
    point = (10, 20)
    print("Point:", point)
    print("X:", point[0])
    print("Y:", point[1])

    x, y = point
    print(f"Unpacked coordinates: x={x}, y={y}")

    rgb = (255, 128, 0)
    print("RGB:", rgb)

    # A one-item tuple needs a trailing comma.
    single_item = ("Python",)
    print("Single-item tuple:", single_item)

    # Tuples cannot be modified in place. Create a new tuple instead.
    updated_point = (point[0], 99)
    print("Updated point:", updated_point)


if __name__ == "__main__":
    main()
