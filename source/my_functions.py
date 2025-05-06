from shapes.square import Square


def add(number_one, number_two):
    return number_one + number_two


def main():
    a = Square(2, 2)
    print(a.get_opp())
    a.get_type()


if __name__ == "__main__":
    main()
