from room import Room
from player import Player

# Declare how players move


# Declare all the rooms
# Dictionary of rooms mapping name to Room
room = {
    'outside':  Room("Outside Cave Entrance",
                     "\n North of you, the cave mount beckons \n"),

    'foyer':    Room("Foyer", """\n Dim light filters in from the south. Dusty
passages run north and east. \n"""),

    'overlook': Room("Grand Overlook", """\n A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. \n"""),

    'narrow':   Room("Narrow Passage", """\n The narrow passage bends here from west
to north. The smell of gold permeates the air. \n"""),

    'treasure': Room("Treasure Chamber", """\n You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. \n"""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
welcome = input("Welcome, would you like to play? (yes/no) ")
if welcome.lower().strip() == "yes":
    player_name = input("\n What should I call you?: ")
    print(f"\n Welcome to the game: {player_name}")
# Make a new player object that is currently in the 'outside' room.
    player = Player(player_name, room['outside'])
    required = ("\n Use only 'n', 's', 'e', 'w' when making a choice\n")
    invalid_entry = (
        "\n There's nothing over there...look a different direction\n")
# Write a loop that:
    while True:
        # * Prints the current room name
        current_room = player.current_room
        print(f"\n Current Location: {player.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
        print(player.current_room.description)
    # * Waits for user input and decides what to do.
        user_input = input(
            "Where would you like to go? [n] north, [s] south, [e] east, [w] west OR [q] quit:\n")

    # If the user enters a cardinal direction, attempt to move to the room there.
# OUTSIDE
        if user_input == "n":
            if hasattr(current_room, "n_to"):
                # if current_room.n_to is not None:
                player.current_room = getattr(current_room, "n_to")
                # player1.current_room = current_room.n_to
            else:
                pass

            attribute = user_input + "_to"
    # Print an error message if the movement isn't allowed.
    # If the user enters "q", quit the game.
        elif user_input == "q":
            print("\nLeaving so soon?")
            break
    # Print an error message if the movement isn't allowed.
        else:
            print(invalid_entry)

# FOYER
        if user_input == "n":
            if hasattr(current_room, "n_to"):
                # if current_room.n_to is not None:
                player.current_room = getattr(current_room, "n_to")
                # player1.current_room = current_room.n_to
            else:
                pass

            attribute = user_input + "_to"
    # Print an error message if the movement isn't allowed.
        elif user_input == "q":
            print("\nLeaving so soon?")
            break
    # If the user enters "q", quit the game.
        else:
            print(invalid_entry)
else:
    print("\n Fine then...but if you have the courage to play sometime, type 'yes' \n")

# PLAN
# 1) Create room class with name & description
# - rooms are already linked
# 2) create a player object

# How do we move?
