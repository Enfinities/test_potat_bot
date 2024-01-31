from datetime import datetime

import pytest
from potato_functions import fix_old_potatoes  # Replace 'your_module' with the actual module name

def test_fix_old_potatoes():
    # Example input
    potatoes_list = [
        {'name': 'Potato 1', 'owner_discord_id': 123456789, 'date': '2022-01-01'},
        {'name': 'Potato 2', 'owner_discord_id': 987654321, 'date': '2022-01-02'},
        {'name': 'Potato 3', 'owner_discord_id': 456789123, 'date': '2022-01-03'}
    ]

    # Calling the function
    updated_potatoes = fix_old_potatoes(potatoes_list)

    # Assertions
    assert len(updated_potatoes) == len(potatoes_list)

    for updated_potato in updated_potatoes:
        assert 'date' in updated_potato
        assert isinstance(updated_potato['date'], str)
        assert len(updated_potato['date']) == 19  # yyyy-mm-dd hh:mm:ss

        # Check if the date string can be converted to a datetime object
        try:
            datetime.strptime(updated_potato['date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            pytest.fail("Invalid date string format")

# Run the tests
if __name__ == "__main__":
    pytest.main()