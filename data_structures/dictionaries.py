"""Dictionary operations: lookup, update, iteration, and counting."""


def main():
    person = {"name": "Maya", "age": 24}
    print("Name:", person["name"])
    print("City:", person.get("city", "Unknown"))

    person["city"] = "Kochi"
    person.update({"age": 25, "role": "Developer"})
    print("Updated person:", person)

    print("\nFields:")
    for key, value in person.items():
        print(f"{key}: {value}")

    del person["role"]
    print("\nAfter deleting role:", person)

    sentence = "python makes practice productive"
    word_counts = {}
    for word in sentence.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    print("\nWord counts:", word_counts)


if __name__ == "__main__":
    main()
