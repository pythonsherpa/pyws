"""
Type hinting exercise
"""


def main() -> None:
    """Simple program for illustrative purposes"""
    age = ask_user_age()
    print_age(age)


def ask_user_age() -> int:
    """Return user input"""
    age = int(input("What is your age in years? "))
    return age


def print_age(age: int) -> None:
    """Print full sentence"""
    age_in_months = age * 12
    print(f"You are {age_in_months} months old.")


if __name__ == "__main__":
    main()
