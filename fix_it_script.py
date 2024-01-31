import potato_functions
import potato_user_interface
potato_functions.pull_database()
from datetime import datetime
def fix_old_potatoes(potatoes):
    counter_seconds = 0
    counter_minutes = 0

    for potato in potatoes:
        if 'date' in potato and isinstance(potato['date'], str) and len(potato['date']) == 10 and potato['date'].count(
                '-') == 2:
            try:
                # Convert the date string to a datetime object
                date_object = datetime.strptime(potato['date'], '%Y-%m-%d')

                # Update the datetime object with counters
                updated_date = date_object.replace(hour=0, minute=counter_minutes, second=counter_seconds)

                # Increment counters
                counter_seconds += 1
                if counter_seconds == 60:
                    counter_seconds = 0
                    counter_minutes += 1

                # Update the potato in the list
                potato['date'] = updated_date.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                # Ignore invalid date strings
                pass

    return potatoes


# Example usage:
potatoes_list = [
    {'name': 'Potato 1', 'owner_discord_id': 123456789, 'date': '2022-01-01'},
    {'name': 'Potato 2', 'owner_discord_id': 987654321, 'date': '2022-01-02'},
    {'name': 'Potato 3', 'owner_discord_id': 456789123, 'date': '2022-01-03'}
]

updated_potatoes = fix_old_potatoes(potatoes_list)
print(updated_potatoes)

fix = fix_old_potatoes(potato_user_interface.all_potatoes)
potato_user_interface.all_potatoes = fix
potato_functions.save_potatoes(potato_user_interface.all_potatoes, potato_functions.database_filename)
potato_functions.push_database("update complete")
print("update complete")