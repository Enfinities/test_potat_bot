import pytest
from potato_functions import delete_potato

# Sample potato data
all_potatoes = [
    {'name': 'Potato 1', 'owner_discord_id': 123456789},
    {'name': 'Potato 2', 'owner_discord_id': 987654321},
    {'name': 'Potato 3', 'owner_discord_id': 123456789},
    {'name': 'Potato 4', 'owner_discord_id': 987654321},
    {'name': 'Potato 5', 'owner_discord_id': 123456789},
]

# Test case: Delete potatoes that exist in the list of all potatoes
def test_delete_potato_existing_potatoes():
    potatoes_to_delete = [{'name': 'Potato 1', 'owner_discord_id': 123456789},
                          {'name': 'Potato 3', 'owner_discord_id': 123456789},
                          {'name': 'Potato 5', 'owner_discord_id': 123456789}]
    result = delete_potato(potatoes_to_delete, all_potatoes)
    expected_result = [{'name': 'Potato 2', 'owner_discord_id': 987654321},
                       {'name': 'Potato 4', 'owner_discord_id': 987654321}]
    assert result == expected_result

# Test case: Delete potatoes that do not exist in the list of all potatoes
def test_delete_potato_non_existing_potatoes():
    potatoes_to_delete = [{'name': 'Potato X', 'owner_discord_id': 123456789},
                          {'name': 'Potato Y', 'owner_discord_id': 987654321}]
    result = delete_potato(potatoes_to_delete, all_potatoes)
    assert result == all_potatoes  # List remains unchanged

# Test case: Mixed scenario with some existing and some non-existing potatoes to delete
def test_delete_potato_mixed_scenario():
    potatoes_to_delete = [{'name': 'Potato 1', 'owner_discord_id': 123456789},
                          {'name': 'Potato X', 'owner_discord_id': 987654321},
                          {'name': 'Potato 5', 'owner_discord_id': 123456789},
                          {'name': 'Potato Y', 'owner_discord_id': 987654321}]
    result = delete_potato(potatoes_to_delete, all_potatoes)
    expected_result = [{'name': 'Potato 2', 'owner_discord_id': 987654321},
                       {'name': 'Potato 3', 'owner_discord_id': 123456789},
                       {'name': 'Potato 4', 'owner_discord_id': 987654321}]
    assert result == expected_result
