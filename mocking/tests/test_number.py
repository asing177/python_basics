import pytest
from unittest import mock
from mocking.guess import guess_number


@mock.patch("mocking.guess.roll_dice")
def test_guess_number(mock_dice):
    mock_dice.return_value = 4
    assert guess_number(4) == True

@pytest.mark.parametrize("_input, expected" , [(3, False), (4, True)])
@mock.patch("mocking.guess.roll_dice")
def test_guess_parameterized(mock_dice, _input ,expected):
    mock_dice.return_value = 4
    assert guess_number(_input) == expected

