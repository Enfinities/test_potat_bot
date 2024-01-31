import pytest
from potato_functions import delete_potato
from datetime import datetime, timedelta

# Sample potato data with unique datetimes
current_datetime = datetime.now()

potato1 = {'name': 'Potato 1', 'owner_discord_id': 123456789, 'date': current_datetime}
potato2 = {'name': 'Potato 2', 'owner_discord_id': 987654321, 'date': current_datetime + timedelta(days=1)}
potato3 = {'name': 'Potato 3', 'owner_discord_id': 123456789, 'date': current_datetime + timedelta(days=2)}
potato4 = {'name': 'Potato 4', 'owner_discord_id': 987654321, 'date': current_datetime + timedelta(days=3)}
potato5 = {'name': 'Potato 5', 'owner_discord_id': 123456789, 'date': current_datetime + timedelta(days=4)}
potato6 = {'name': 'Potato 6', 'owner_discord_id': 987654321, 'date': current_datetime + timedelta(days=5)}
potato7 = {'name': 'Potato 7', 'owner_discord_id': 123456789, 'date': current_datetime + timedelta(days=6)}
potatoX = {'name': 'Potato X', 'owner_discord_id': 1, 'date': current_datetime.strftime('%Y-%m-%d %H:%M:%S')}
potatoY = {'name': 'Potato Y', 'owner_discord_id': 2, 'date': current_datetime.strftime('%Y-%m-%d %H:%M:%S')}

all_potatoes = [potato1, potato2, potato3, potato4, potato5, potato6, potato7]
for potato in all_potatoes:
    potato['date'] = potato['date'].strftime('%Y-%m-%d %H:%M:%S')

# Test case: Delete potatoes that exist in the list of all potatoes
def test_delete_potato_existing_potatoes():
    potatoes_to_delete = [potato1, potato3, potato5]
    result = delete_potato(potatoes_to_delete, all_potatoes)
    expected_result = [potato2, potato4, potato6, potato7]
    assert result == expected_result

# Test case: Delete potatoes that do not exist in the list of all potatoes
def test_delete_potato_non_existing_potatoes():
    potatoes_to_delete = [potatoX,potatoY]
    result = delete_potato(potatoes_to_delete, all_potatoes)
    assert result == all_potatoes  # List remains unchanged

# Test case: Mixed scenario with some existing and some non-existing potatoes to delete
def test_delete_potato_mixed_scenario():
    potatoes_to_delete = [potato1, potatoX, potato5, potatoY]
    result = delete_potato(potatoes_to_delete, all_potatoes)
    expected_result = [potato2, potato3, potato4, potato6, potato7]
    assert result == expected_result
