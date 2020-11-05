from mocking.dice import roll_dice


def guess_number(num):
    roll = roll_dice()
    print(roll)
    if roll == num:
        return True
    else:
        return False


print(guess_number(4))