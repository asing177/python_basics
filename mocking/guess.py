from mocking.dice import roll_dice


def guess_number(num):
    roll = roll_dice()
    if roll == num:
        return True
    else:
        return False