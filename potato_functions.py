import json

def create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date):
        potato = {"owner_name": owner_name,"owner_discord_id": owner_discord_id,"name": name,"potato_type": potato_type,"price": price,"accomplishment": accomplishment,"date": date}
        return potato

def read_potatos_by_discord_id(a,b):
    # logic for how to find info here
    result_potatoes = []
    for potato in a:
        if potato['owner_discord_id'] == b:
            result_potatoes.append(potato)

    return(result_potatoes)


def load_potatoes(save_filename):
    with open(save_filename, 'r') as file:
        loaded_potatoes = json.load(file)

    return (loaded_potatoes)
def save_potatoes(potatoes,save_filename):
    potatoes = {
        "owner_name": owner_name
        "owner_discord_id": owner_discord_id
        "name": name
        "potato_type": potato_type
        "price": price
        "accomplishment": accomplishment
        "date": date
    }
    with open(save_filename, 'w') as outfile:
        json.dump(potatoes,outfile)

    return potatoes
def update_potato():

    # logic for how to find info here.
    pass

def delete_potato():
    # logic for how to find info here.
    pass

import os

def file_exists(file_path):
    """
    Check if a file exists.

    Args:
    - file_path (str): The path to the file.

    Returns:
    - bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)
