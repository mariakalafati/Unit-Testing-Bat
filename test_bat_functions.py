import pytest
from bat_functions import calculate_bat_power

# Test 1a: calculate_bat_power - testing various level values (positive, zero, negative)
def test_calculate_bat_power():
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(-2) == -84