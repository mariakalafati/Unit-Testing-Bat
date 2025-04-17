# Unit Testing Bat-Tech with Pytest

Lab Assignment 2 for the "Software Engineering in Practice" course at the Department of Management Science and Technology, Athens University of Economics and Business.

## Overview
This repository contains a project that demonstrates the use of **pytest** to write clean, modular, and powerful tests for a Python module (`bat_functions.py`). The testing suite ensures Batman's tools run flawlessly — no bugs, no delays, no mischief.

## Objectives Completed

### 1. Basic Tests & Parametrization
- Wrote unit tests for `calculate_bat_power`  
- Used **parametrization** to test `signal_strength` with various distances

### 2. Using Fixtures
- Created a reusable fixture for Bat vehicle data  
- Tested `get_bat_vehicle` for valid and invalid inputs

### 3. Mocking External Dependencies
- Mocked `fetch_joker_info` to simulate an instant response  
- Verified mock returns a custom result without waiting for real delay

### 4. Continuous Integration
- Configured GitHub Actions to:
  - Run `pytest` on **every push or pull request**
  - Use **Ubuntu** and **Python 3.10.17**
  - Automatically install dependencies and execute tests
 
## Licence
The project is under the Apache 2.0 Licence 

