from potato_functions import read_potatoes_by_discord_id

# Replace 'potato_functions' with the actual module where the read_potatos_by_discord_id function is defined


# Test case when there are multiple Potatoes with the same discord_id
def test_read_potatoes_by_discord_id_multiple_matches():
    potatoes = [
        {'owner_name': 'John Doe', 'owner_discord_id': 123456789, 'name': 'Achievement 1', 'potato_type': 'Personal', 'price': 10.5, 'accomplishment': 'Completed task', 'date': '2024-01-08'},
        {'owner_name': 'Alice Smith', 'owner_discord_id': 123456789, 'name': 'Milestone 2', 'potato_type': 'Professional', 'price': 20.0, 'accomplishment': 'Exceeded target', 'date': '2024-01-10'},
    ]

    # Call the read_potatos_by_discord_id function
    result_potatoes = read_potatoes_by_discord_id(potatoes, 123456789)

    # Check if the result is a list
    assert isinstance(result_potatoes, list)

    # Check if all Potatoes in the result have the correct discord_id
    for potato in result_potatoes:
        assert potato['owner_discord_id'] == 123456789


# Test case when there is a single Potato with the given discord_id
def test_read_potatoes_by_discord_id_single_match():
    potatoes = [
        {'owner_name': 'John Doe', 'owner_discord_id': 987654321, 'name': 'Milestone 1', 'potato_type': 'Personal', 'price': 12.0, 'accomplishment': 'Completed project', 'date': '2024-01-10'},
    ]

    # Call the read_potatos_by_discord_id function
    result_potatoes = read_potatoes_by_discord_id(potatoes, 987654321)

    # Check if the result is a list containing a single Potato with the correct discord_id
    assert isinstance(result_potatoes, list)
    assert len(result_potatoes) == 1
    assert result_potatoes[0]['owner_discord_id'] == 987654321


# Test case when there are no Potatoes with the given discord_id
def test_read_potatoes_by_discord_id_no_match():
    potatoes = [
        {'owner_name': 'John Doe', 'owner_discord_id': 123456789, 'name': 'Achievement 1', 'potato_type': 'Personal', 'price': 10.5, 'accomplishment': 'Completed task', 'date': '2024-01-08'},
        {'owner_name': 'Alice Smith', 'owner_discord_id': 987654321, 'name': 'Milestone 1', 'potato_type': 'Professional', 'price': 15.75, 'accomplishment': 'Reached a goal', 'date': '2024-01-09'},
    ]

    # Call the read_potatos_by_discord_id function for a nonexistent discord_id
    result_potatoes = read_potatoes_by_discord_id(potatoes, 999999999)

    # Check if the result is None since there are no Potatoes with the given discord_id
    assert result_potatoes == []
