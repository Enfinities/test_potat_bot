import json
from pathlib import Path
import git
database_filename = "my_potatoes.json"

def create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date):
        potato = {"owner_name": owner_name,"owner_discord_id": owner_discord_id,"name": name,"potato_type": potato_type,"price": price,"accomplishment": accomplishment,"date": date}
        return potato

def read_potatoes_by_discord_id(potatoes,owner_discord_id):
    # logic for how to find info here
    result_potatoes = []
    for potato in potatoes:
        if potato['owner_discord_id'] == owner_discord_id:
            result_potatoes.append(potato)

    return(result_potatoes)


def load_potatoes(save_filename):
    with open(save_filename, 'r') as file:
        loaded_potatoes = json.load(file)

    return (loaded_potatoes)
def save_potatoes(potatoes,save_filename):
    with open(save_filename, 'w') as file:
        json.dump(potatoes,file)

    return potatoes
def update_potato():

    # logic for how to find info here.
    pass

def delete_potato():
    # logic for how to find info here
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


def format_achievements(achievements):
    owner_achievements = {}

    for achievement in achievements:
        owner_name = achievement['owner_name']

        if owner_name not in owner_achievements:
            owner_achievements[owner_name] = []

        owner_achievements[owner_name].append(achievement)

    formatted_output = ""

    for owner_name, achievements_list in owner_achievements.items():
        formatted_output += f"# {owner_name}\n"

        for achievement in achievements_list:
            formatted_output += f"- name: {achievement['name']}\n"
            formatted_output += f"- potato_type: {achievement['potato_type']}\n"
            formatted_output += f"- price: ${achievement['price']}\n"
            formatted_output += f"- accomplishment: {achievement['accomplishment']}\n"
            formatted_output += f"- date: {achievement['date']}\n\n"

    return formatted_output

def pull_database():
    current_directory = Path.cwd()
    repo = git.Repo(str(current_directory))
    origin = repo.remote("origin")
    origin.fetch()

    repo.git.pull(origin, repo.head.ref)

    print("Database pulled")


def push_database(commit_message):
    current_directory = Path.cwd()
    repo = git.Repo(str(current_directory))
    origin = repo.remote("origin")
    origin.fetch()
    repo.index.add([database_filename])
    repo.index.commit(commit_message)
    repo.git.push(origin, repo.head.ref)
    print("database pushed")

    #and this is the function that passes the tests, which can be added to the bottom of potato_functions.py

def discord_post_resizer(input_str):
    # Check if the input is not a string type
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")

    # Check if the input is None or an empty string
    if len(input_str) == 0:
        return []

    # Initialize the result list
    result = []

    # Process the input string in chunks of 2000 characters or less
    while len(input_str) > 0:
        if len(input_str) <= 2000:
            # If the remaining string is 2000 characters or less, add it to the result
            result.append(input_str)
            break

        # Find a suitable position to split the string
        split_pos = 2000

        # Iterate backward from 2000 to 1000
        for i in range(2000, 1000, -1):
            if input_str[i] == '\n':
                split_pos = i + 1
                break

        # If no newline found, check for a period
        if split_pos == 2000:
            for i in range(2000, 1000, -1):
                if input_str[i] == '.':
                    split_pos = i + 1
                    break

        # If still no period found, check for a space
        if split_pos == 2000:
            for i in range(2000, 1000, -1):
                if input_str[i] == ' ':
                    split_pos = i + 1
                    break

        # Append the chunk to the result and remove it from the input string
        result.append(input_str[:split_pos])
        input_str = input_str[split_pos:]

    return result