import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle

# Test 1a: calculate_bat_power - testing various level values (positive, zero, negative)
def test_calculate_bat_power():
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(5) == 210
    assert calculate_bat_power(-2) == -84


# Test 1b: signal_strength with parameterization - testing various cases (normal, mid, edge, negative)
@pytest.mark.parametrize(
    "distance, expected_strength",
    [(0, 100), (5, 50), (10, 0), (12, 0)]
)
def test_signal_strength(distance, expected_strength):
    assert signal_strength(distance) == expected_strength


# Test 2: fixture for bat vehicles - dictionary of expected values
@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }