import pytest
from potato_functions import find_potato

# Sample potato data
potatoes = [
    {'date': '2024-01-08', 'owner_discord_id': 123456789},
    {'date': '2024-01-09', 'owner_discord_id': 987654321},
    {'date': '2024-01-09', 'owner_discord_id': 123456789},
    {'date': '2024-01-09', 'owner_discord_id': 987654321},
    {'date': '2024-01-10', 'owner_discord_id': 987654321},
    {'date': '2024-01-10', 'owner_discord_id': 123456789},
    {'date': '2024-01-09 15:45:00', 'owner_discord_id': 987654321},
    {'date': '2024-01-08 12:30:00', 'owner_discord_id': 123456789},
    {'date': '2024-01-09 15:45:00', 'owner_discord_id': 987654321},
    {'date': '2024-01-09 18:20:00', 'owner_discord_id': 123456789},
    {'date': '2024-01-10 08:10:00', 'owner_discord_id': 987654321},
    {'date': '2024-01-10 10:25:00', 'owner_discord_id': 123456789},
]


# Test case: No matching potato exists
def test_find_potato_no_match():
    result = find_potato('2024-01-11', 123456789, potatoes)
    assert result == []


# Test case: One matching potato exists
def test_find_potato_one_match():
    result = find_potato('2024-01-08', 123456789, potatoes)
    assert result == [{'date': '2024-01-08', 'owner_discord_id': 123456789}]


# Test case: Multiple matching potatoes exist
def test_find_potato_multiple_matches():
    result = find_potato('2024-01-09', 987654321, potatoes)
    expected_result = [
        {'date': '2024-01-09', 'owner_discord_id': 987654321},
        {'date': '2024-01-09', 'owner_discord_id': 987654321},
    ]
    assert result == expected_result


# Test case: No matching potato exists
def test_find_potato_no_match_datetime_format():
    result = find_potato('2024-01-11 14:30:00', 123456789, potatoes)
    assert result == []


# Test case: One matching potato exists
def test_find_potato_one_match_datetime_format():
    result = find_potato('2024-01-08 12:30:00', 123456789, potatoes)
    assert result == [{'date': '2024-01-08 12:30:00', 'owner_discord_id': 123456789}]


# Test case: Multiple matching potatoes exist
def test_find_potato_multiple_matches_datetime_format():
    result = find_potato('2024-01-09 15:45:00', 987654321, potatoes)
    expected_result = [
        {'date': '2024-01-09 15:45:00', 'owner_discord_id': 987654321},
        {'date': '2024-01-09 15:45:00', 'owner_discord_id': 987654321}
    ]
    assert result == expected_result
