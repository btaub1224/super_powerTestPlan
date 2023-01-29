from super_power import super_power
from random import randint

def test_happy_path():
    x = randint(0, 1000)
    power_x = x * x
    print("%s^2 = %s" % (x, super_power(x)))
    assert super_power(x) == power_x, f"x^2 value returned incorrect, super_power returned {super_power(x)}, manually recieved {power_x}"

test_happy_path()