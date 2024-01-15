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

import json
def loaded_potatoes(saved_filename):
    with open(save_filename, 'r') as file:
        loaded_potatoes = json.load(file)

    return (loaded_potatoes)
def update_potato():

    # logic for how to find info here
    pass

def delete_potato():
    # logic for how to find info here.
    pass