def main():
    name = input("What is your name? ")
    greet(name)


def greet(name):
    print("Hello %s, how are you?" % name)
    print("Hello {}, how are you".format(name))
    print(f"Hello {name}, how are you")
    return


def make_percentage(number):
    percentage = number / 100
    pass
    return f"{percentage}%"


if __name__ == "__main__":
    main()
