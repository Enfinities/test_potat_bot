import pytest
from potato_functions import discord_post_resizer


# Test case for a string of 6000 characters with specific newline positions
def test_discord_post_resizer_input_with_newlines():
    input_str = "A" * 1499 + "\n" + "B" * 1699 + "\n" + "C" * 1049 + "\n" + "D" * 1749
    result = discord_post_resizer(input_str)

    expected_result = [
        "A" * 1499 + "\n",        # First entry with 1499 characters
        "B" * 1699 + "\n",        # Second entry with 1699 characters
        "C" * 1049 + "\n",        # Third entry with 1049 characters
        "D" * 1749         # Fourth entry with 1749 characters
    ]

    assert result == expected_result


# Test case for an empty input
def test_discord_post_resizer_empty_input():
    result = discord_post_resizer("")
    assert result == []


# Test case for input of 2000 characters or fewer
def test_discord_post_resizer_input_under_2000_characters():
    input_str = "This is a short string."
    result = discord_post_resizer(input_str)
    assert result == [input_str]


# Test case for non-string input
def test_discord_post_resizer_non_string_input():
    with pytest.raises(ValueError):
        discord_post_resizer(123)  # Non-string input should raise a ValueError


# Test case for input of 2001 characters
def test_discord_post_resizer_input_2001_characters():
    input_str = "A" * 2001
    result = discord_post_resizer(input_str)
    expected_result = ["A" * 2000, "A"]
    assert result == expected_result


# Test case for input of 4000 characters
def test_discord_post_resizer_input_4000_characters():
    input_str = "B" * 4000
    result = discord_post_resizer(input_str)
    expected_result = ["B" * 2000, "B" * 2000]
    assert result == expected_result


# Test case for input of 6000 characters
def test_discord_post_resizer_input_6000_characters():
    input_str = "C" * 6000
    result = discord_post_resizer(input_str)
    expected_result = ["C" * 2000, "C" * 2000, "C" * 2000]
    assert result == expected_result
