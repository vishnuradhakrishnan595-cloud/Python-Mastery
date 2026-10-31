"""Function definitions, defaults, keyword-only args, *args, and **kwargs."""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def add(a: float, b: float = 0) -> float:
    """Add two numbers."""
    return a + b


def calculate_discount(price: float, percent: float) -> float:
    """Return a price after applying a percentage discount."""
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not 0 <= percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")
    return price * (1 - percent / 100)


def total(*numbers: float) -> float:
    """Add any number of positional numeric arguments."""
    return sum(numbers)


def describe_user(name: str, *, city: str = "Unknown", active: bool = True) -> str:
    """Demonstrate keyword-only arguments."""
    return f"{name} | city={city} | active={active}"


def show_details(**details) -> None:
    """Print arbitrary keyword details."""
    for key, value in details.items():
        print(f"{key}: {value}")


def main():
    print(greet("Vishnu"))
    print("Add:", add(5, 2))
    print("Add with default:", add(5))
    print("Discounted price:", calculate_discount(2000, 15))
    print("Total:", total(10, 20, 30))
    print(describe_user("Asha", city="Kochi", active=True))
    show_details(role="Software Engineer", language="Python")


if __name__ == "__main__":
    main()
