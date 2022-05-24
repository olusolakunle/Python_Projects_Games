import random


def play():
    """
    Player is required to type either r or s or p
    :return:
    """

    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You WON!'

    return 'You Lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())