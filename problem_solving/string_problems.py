"""String challenges: palindrome, vowels, anagrams, and word reversal."""


def is_palindrome(text: str) -> bool:
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(text: str) -> int:
    vowels = set("aeiou")
    return sum(1 for char in text.lower() if char in vowels)


def are_anagrams(first: str, second: str) -> bool:
    normalize = lambda value: sorted(
        char.lower() for char in value if char.isalnum()
    )
    return normalize(first) == normalize(second)


def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])


def character_frequency(text: str) -> dict[str, int]:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def main():
    print("Palindrome:", is_palindrome("Never odd or even"))
    print("Vowels:", count_vowels("Python Programming"))
    print("Anagrams:", are_anagrams("listen", "silent"))
    print("Reversed words:", reverse_words("Python is fun"))
    print("Character frequency:", character_frequency("banana"))


if __name__ == "__main__":
    main()
