"""Inheritance example: shared base behavior and specialized subclasses."""


class Employee:
    def __init__(self, name: str, employee_id: int):
        self.name = name
        self.employee_id = employee_id

    def describe(self) -> str:
        return f"{self.name} (ID: {self.employee_id})"


class Developer(Employee):
    def __init__(self, name: str, employee_id: int, language: str):
        super().__init__(name, employee_id)
        self.language = language

    def describe(self) -> str:
        return f"{super().describe()} — Developer using {self.language}"


class Designer(Employee):
    def __init__(self, name: str, employee_id: int, tool: str):
        super().__init__(name, employee_id)
        self.tool = tool

    def describe(self) -> str:
        return f"{super().describe()} — Designer using {self.tool}"


def main():
    team = [
        Developer("Asha", 101, "Python"),
        Designer("Ravi", 102, "Figma"),
    ]

    for employee in team:
        print(employee.describe())


if __name__ == "__main__":
    main()
