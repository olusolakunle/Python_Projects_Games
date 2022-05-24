def hello(name: str):
    print("Hello {}!".format(name))
    print(f'Hello {name}!')


hello("Zahra")


def add_num(x, y):
    return x + y


result = add_num(3.33, 5.4)
print(f'The value is {result}cm')


def print_tree(char1: str, char2: str):
    """

    :param char1: takes any character in string
    :param char2: takes any character in string
    :return: print the tree
    """
    for x in range(10):
        if x % 2 != 0:
            text = char1 * x
            left_margin = (10 - len(text)) // 2
            print(" " * left_margin, text)
    print(" " * (left_margin + 3), char2)
    print(" " * (left_margin + 3), char2)


print_tree('^', '||')
