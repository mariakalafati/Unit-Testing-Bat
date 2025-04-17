import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

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

# Test 2a: get_bat_vehicle known - parametrized test to verify specifications 
@pytest.mark.parametrize("vehicle_name", ["Batmobile", "Batwing", "Batcycle"])
def test_get_bat_vehicle_known(vehicle_name, bat_vehicles):
    assert get_bat_vehicle(vehicle_name) == bat_vehicles[vehicle_name]


# Test 2b: get_bat_vehicle unknown - verify that unknown vehicle names trigger ValueError
def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError, match="Unknown vehicle:.*"):
        get_bat_vehicle("Batboat")


# Test 3: mock fetch_joker_info - simulate a fast response, custom directory, verify
def test_fetch_joker_info_mocked(monkeypatch):
    def fake_fetch():
        return {'mischief_level': 0, 'location': 'captured'}
    monkeypatch.setattr("bat_functions.fetch_joker_info", fake_fetch)
    assert fetch_joker_info() == {'mischief_level': 0, 'location': 'captured'}