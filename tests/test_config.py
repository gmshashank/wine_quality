import pytest


class notInRange(Exception):
    def __init__(self, message="Value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(notInRange):
        if a not in range(10, 20):
            raise notInRange

def test_abc():
    a=5
    b=5
    assert True