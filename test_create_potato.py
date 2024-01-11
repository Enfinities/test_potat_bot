from potato_functions import create_potato


def test_create_potato_returns_a_dict():
    owner_name = "John Doe"
    owner_discord_id = 123456789
    name = "Demo Achievement"
    potato_type = "Demo Type"
    price = 8.99
    accomplishment = "Demo Accomplishment"
    date = "2024-01-10"

    potato = create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date)

    assert isinstance(potato, dict)


def test_create_potato_has_correct_keys():
    owner_name = "John Doe"
    owner_discord_id = 123456789
    name = "Demo Achievement"
    potato_type = "Demo Type"
    price = 8.99
    accomplishment = "Demo Accomplishment"
    date = "2024-01-10"

    potato = create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date)
    assert set(potato.keys()) == {'owner_name', 'owner_discord_id', 'name', 'potato_type', 'price', 'accomplishment', 'date'}


def test_create_potato_properly_sets_owner_name():
    owner_name = "John Doe"
    owner_discord_id = 123456789
    name = "Demo Achievement"
    potato_type = "Demo Type"
    price = 8.99
    accomplishment = "Demo Accomplishment"
    date = "2024-01-10"

    potato = create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date)
    assert potato['owner_name'] == owner_name
    assert potato['owner_discord_id'] == owner_discord_id
    assert potato['name'] == name
    assert potato['potato_type'] == potato_type
    assert potato['price'] == price
    assert potato['accomplishment'] == accomplishment


def test_create_potato_properly_sets_date():
    owner_name = "John Doe"
    owner_discord_id = 123456789
    name = "Demo Achievement"
    potato_type = "Demo Type"
    price = 8.99
    accomplishment = "Demo Accomplishment"
    date = "2024-01-10"

    potato = create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date)
    assert potato['date'] == date
