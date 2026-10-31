"""Conditional statements and simple validation."""


def grade_from_score(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 40:
        return "D"
    return "Needs improvement"


def main():
    score = 82
    print(f"Score: {score}; grade: {grade_from_score(score)}")

    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"Age {age}: {status}")

    number = -4
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


if __name__ == "__main__":
    main()
