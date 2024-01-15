import os
import json
import pytest
from potato_functions import save_potatoes, load_potatoes

# Replace 'potato_functions' with the actual module where the functions are defined

# Test case for saving and loading potatoes using the json module
def test_save_and_load_potatoes():

    # Test data
    potatoes = [
        {'owner_name': 'John Doe', 'owner_discord_id': 123456789, 'name': 'Achievement 1', 'potato_type': 'Personal', 'price': 10.5, 'accomplishment': 'Completed task', 'date': '2024-01-08'},
        {'owner_name': 'Alice Smith', 'owner_discord_id': 987654321, 'name': 'Milestone 1', 'potato_type': 'Professional', 'price': 15.75, 'accomplishment': 'Reached a goal', 'date': '2024-01-09'},
    ]

    # Save potatoes to a file
    save_filename = 'test_potatoes.json'
    save_potatoes(potatoes, save_filename)

    # Load potatoes from the saved file
    loaded_potatoes = load_potatoes(save_filename)

    # Check if the loaded potatoes match the original ones
    assert loaded_potatoes == potatoes


# Test case for loading potatoes from a non-existent file
def test_load_potatoes_nonexistent_file():

    # Non-existent file path
    nonexistent_filename = 'nonexistent_file.json'

    # Attempt to load potatoes from a non-existent file
    with pytest.raises(FileNotFoundError):
        load_potatoes(nonexistent_filename)
