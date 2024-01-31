from decouple import config
import interactions
import git
from interactions import (slash_command, SlashContext,
                          SlashCommand, slash_option,
                          OptionType, SlashCommandChoice)
from pathlib import Path
from datetime import datetime
import potato_functions
from potato_functions import database_filename

all_potatoes = []
try:
    all_potatoes = potato_functions.load_potatoes(database_filename)
except:
    pass
# Base command
base_command = SlashCommand(
    name="potato",
    description="Commands involving potatoes"
)


@base_command.subcommand(sub_cmd_name="create_potato", sub_cmd_description="Create a potato.")
@slash_option(name="potato_name", required=True, description="Name of potato. e.g breaking stuff", opt_type=OptionType.STRING)
@slash_option(name="potato_type", required=True, description="Type of potato. e.g. coding, books, or gaming", opt_type=OptionType.STRING)
@slash_option(name="potato_price", required=True, description="How much do you value it, in terms of dollars?. e.g. 2.50", opt_type=OptionType.NUMBER)
@slash_option(name="potato_accomplishment", required=True, description="Fuller description of the accomplishment. e.g. I coded for an 3 hours.", opt_type=OptionType.STRING)
async def create_potato(ctx: SlashContext, potato_name: str, potato_type: str, potato_price: str, potato_accomplishment: str):
    user = ctx.author  # Get the user who invoked the command
    potato_functions.pull_database()
    owner_name = user.username.title()
    owner_discord_id = user.id
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    name = potato_name
    potato_type = potato_type
    price = potato_price
    accomplishment = potato_accomplishment

    #################################################
    # Put your code under here
    # 1. Use your create_potato function to make the potato from the inputs
    # 2. Use your save potatoes function to save the potato
    #   - database_filename, on line 9, will keep the name of the file
    # ------HW BELOW------
    # assigns created potatoes to new_potato variable
    # entries from new_potato variable gets added to all_potatoes dictionary
    # saves the list of all potatoes to a json file
    #################################################
    await ctx.defer()
    new_potato = potato_functions.create_potato(owner_name, owner_discord_id, name, potato_type, price, accomplishment, date)
    all_potatoes.append(new_potato)
    potato_functions.save_potatoes(all_potatoes,database_filename)
    potato_functions.push_database(owner_name)

    await ctx.send(f"Owner: {owner_name}\nPotato Name: {name}\n"
                   f"Potato Type: {potato_type}\nPrice: {price}\n"
                   f"Accomplishment: {accomplishment}")


@base_command.subcommand(sub_cmd_name="read_potatoes", sub_cmd_description="See your potatoes.")
async def read_potatoes(ctx: SlashContext):
    user = ctx.author  # Get the user who invoked the command
    owner_name = user.username.title()
    owner_discord_id = user.id

    #################################################
    # Put your code under here
    # 1. Put all_potatoes and the discord ID into your read_potatos function
    # 2. You can send the result back to the user using that await ctx.send function
    #   - Feel free to format it prettily, or just put the potato dictionary in there. Either works.
    #################################################
    potato_by_id = potato_functions.read_potatoes_by_discord_id(all_potatoes, owner_discord_id)
    format = potato_functions.format_achievements(potato_by_id)
    posts = potato_functions.discord_post_resizer(format)
    for post in posts:
        if post:
            await ctx.send(post)

@base_command.subcommand(sub_cmd_name="delete_potato", sub_cmd_description="delete a potato.")
@slash_option(name="potato_id", required=True, description="datetime of potato eg. '2024-03-22 00:40:23'", opt_type=OptionType.STRING)
async def delete_potato(ctx: SlashContext, datetime: str):
    user = ctx.author
    discord_id = ctx.author.id
    potatoes_to_delete = potato_functions.find_potato(datetime,discord_id, all_potatoes)
    potato_functions.delete_potato(potatoes_to_delete, all_potatoes)
    await ctx.send("potato deleted")
if __name__ == "__main__":
    try:
        all_potatoes = potato_functions.load_potatoes(database_filename)
    except FileNotFoundError:
        pass
    bot = interactions.Client(token=config("BOT_TOKEN"))
    bot.start()
    potato_functions.pull_database()
