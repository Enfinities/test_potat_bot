from potato_functions import create_potato


def test_create_potato_demo():
    # Input values for a demo test
    owner_name = "John Doe"
    owner_discord_id = 123456789
    name = "Demo Achievement"
    potato_type = "Demo Type"
    price = 8.99
    accomplishment = "Demo Accomplishment"
    date = "2024-01-10"

    # Call the create_potato function
    potato = create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date)

    # Check if the output is a dictionary
    assert isinstance(potato, dict)

    # Check if all expected keys are present in the output dictionary
    assert set(potato.keys()) == {'owner_name', 'owner_discord_id', 'name', 'potato_type', 'price', 'accomplishment', 'date'}

    # Check if each key is mapped to the corresponding input value
    assert potato['owner_name'] == owner_name
    assert potato['owner_discord_id'] == owner_discord_id
    assert potato['name'] == name
    assert potato['potato_type'] == potato_type
    assert potato['price'] == price
    assert potato['accomplishment'] == accomplishment
    assert potato['date'] == date
