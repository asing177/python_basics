import pytest
from unittest import mock
from mocking.get_ip import check_ip


def test_ip():
    assert check_ip() == "0.0.0.0"