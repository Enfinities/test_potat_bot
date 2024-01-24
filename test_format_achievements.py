from potato_functions import format_achievements

def test_format_achievements_single_owner():
    input_data = [
        {'owner_name': 'John Doe', 'owner_discord_id': 123456789, 'name': 'Achievement 1', 'potato_type': 'Personal', 'price': 10.5, 'accomplishment': 'Completed task', 'date': '2024-01-08'},
        {'owner_name': 'John Doe', 'owner_discord_id': 123456789, 'name': 'Achievement 2', 'potato_type': 'Personal', 'price': 10.5, 'accomplishment': 'Completed task', 'date': '2024-01-08'},
    ]

    expected_output = "# John Doe\n- name: Achievement 1\n- potato_type: Personal\n- price: $10.5\n- accomplishment: Completed task\n- date: 2024-01-08\n\n" \
                      "- name: Achievement 2\n- potato_type: Personal\n- price: $10.5\n- accomplishment: Completed task\n- date: 2024-01-08\n\n"

    assert format_achievements(input_data) == expected_output

def test_format_achievements_multiple_owners():
    input_data = [
        {'owner_name': 'John Doe', 'owner_discord_id': 123456789, 'name': 'Achievement 1', 'potato_type': 'Personal', 'price': 10.5, 'accomplishment': 'Completed task', 'date': '2024-01-08'},
        {'owner_name': 'Jane Doe', 'owner_discord_id': 987654321, 'name': 'Achievement 3', 'potato_type': 'Professional', 'price': 15.75, 'accomplishment': 'Successful project', 'date': '2024-01-10'},
    ]

    expected_output = "# John Doe\n- name: Achievement 1\n- potato_type: Personal\n- price: $10.5\n- accomplishment: Completed task\n- date: 2024-01-08\n\n" \
                      "# Jane Doe\n- name: Achievement 3\n- potato_type: Professional\n- price: $15.75\n- accomplishment: Successful project\n- date: 2024-01-10\n\n"

    assert format_achievements(input_data) == expected_output