"""Examples of variables, basic types, conversion, and formatted output."""


def main():
    name = "Vishnu"
    age = 22
    height = 1.72
    is_learning = True
    middle_name = None

    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Learning Python:", is_learning)
    print("Middle name:", middle_name)

    print("\nTypes:")
    for value in (name, age, height, is_learning, middle_name):
        print(value, "->", type(value).__name__)

    age_text = "25"
    converted_age = int(age_text)
    price = float("99.50")

    print(f"\nConverted age: {converted_age}")
    print(f"Price: ₹{price:.2f}")


if __name__ == "__main__":
    main()
