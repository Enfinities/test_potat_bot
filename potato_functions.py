def create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date):
        potato = {"owner_name": owner_name,"owner_discord_id": owner_discord_id,"name": name,"potato_type": potato_type,"price": price,"accomplishment": accomplishment,"date": date}
        return potato

def read_potatos_by_discord_id():
    # logic for how to find info here
    result_potatoes = []
    for potato in potatoes:
        if potato['owner_discord_id'] == discord_id:
            result_potatoes.append(potato)

    print(result_potatoes)

def update_potato():

    # logic for how to find info here.
    pass

def delete_potato():
    # logic for how to find info here.
    pass