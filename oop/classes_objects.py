"""Classes, instances, attributes, methods, and properties."""


class Student:
    school = "Example Academy"

    def __init__(self, name: str, marks: float):
        self.name = name
        self.marks = marks

    def has_passed(self) -> bool:
        return self.marks >= 40

    def summary(self) -> str:
        result = "Passed" if self.has_passed() else "Needs improvement"
        return f"{self.name}: {self.marks} marks — {result}"


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


def main():
    student = Student("Asha", 85)
    print(student.summary())
    print("School:", student.school)

    account = BankAccount("Vishnu", 1000)
    account.deposit(250)
    account.withdraw(100)
    print(f"{account.owner}'s balance: ₹{account.balance:.2f}")


if __name__ == "__main__":
    main()
