################################################################################
# adventure.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
# 28-5-2020
#
# Allows user to play an adventure game: the user has to navigate through a map
# using text based description to find the winning location

from room import Room


class Adventure():

    # create rooms and items for the appropriate 'game' version
    def __init__(self, game):

        # rooms is a dictionary that maps a room number to the corresponding room object
        self.rooms = {}

        # synonymdict is a dictionary that containes synonyms to possible commands
        self.synonymdict = {}

        # read the file with synonyms and store in the dictionary synonymdict
        with open("data/Synonyms.dat") as f:
            while (True):

                # read every line and split into two strings upon equal sign
                syn = f.readline().split("=")

                # stop iterating when it reached newline
                if syn[0] == '\n' or syn[0] == '':
                    False
                    break

                # strip '\n' of the second element in syn
                syn[1] = syn[1].strip("\n")

                # store abbreviation and full command in dictionary
                self.synonymdict[syn[0]] = syn[1]

        # load room structures
        self.load_rooms(f"data/{game}Adv.dat")

        # game always starts in room number 1, so we'll set it after loading
        assert 1 in self.rooms
        self.current_room = self.rooms[1]

    # load rooms from filename in two-step process
    def load_rooms(self, filename):

        # creating rooms
        with open(filename) as f:
            while (True):

                # read every line, remove ''\n' and split upon tab
                line = f.readline().strip("\n").split("\t")

                # stop iterating when it reached newline
                if line[0] == '\n' or line[0] == '':
                    False
                    break

                # save room to self.rooms dictionary
                self.rooms[int(line[0])] = Room(*line)

            # assertions for tinyAdv.dat
            assert 1 in self.rooms
            assert self.rooms[1].name == "Outside building"

            # making connections
            while (True):

                # read every line, remove ''\n', strip of tab and split upon tab
                line = f.readline().strip("\n").strip("\t").split("\t")

                # stop iterating when it reached newline
                if line[0] == '\n' or line[0] == '':
                    False
                    break

                # set first room as source room
                source_room = self.rooms[int(line[0])]

                # save possible next rooms
                for i in range(1, len(line), 2):

                    # set destination room as possible next rooms
                    destination_room = self.rooms[int(line[i + 1])]

                    # update source room
                    source_room.add_connection(line[i], destination_room)

            # assertions for connections between rooms
            assert self.rooms[1].has_connection("WEST")
            assert self.rooms[2].get_connection("EAST").name == "Outside building"

    # pass along the description of the current room
    def get_description(self):

        # if the room has already been visited, return only name
        if self.current_room.already_visited():
            return self.current_room.name

        # if room has not been visited, return full description
        return self.current_room.description

    # move to a different room by changing "current" room, if possible
    def move(self, direction):

        # check if move is possible, if so: move to that room
        if self.current_room.has_connection(direction):
            nextroom = self.current_room.get_connection(direction).room_ID

            # change room to visited
            self.current_room.set_visited()

            # move to nextroom
            self.current_room = self.rooms[int(nextroom)]

            # if move succesfull, return True
            return True

        # if move not possible, return False
        return False

    # return the long description of the current room
    def get_long_description(self):
        return self.current_room.description

    # checks if the next move (belonging to this room) if forced
    def is_forced(self):
        if self.current_room.has_connection("FORCED"):
            return True
        return False


if __name__ == "__main__":

    from sys import argv

    # check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python adventure.py [name]")
        exit(1)

    # load the requested game or else Tiny
    if len(argv) == 1:
        game_name = "Tiny"
    elif len(argv) == 2:
        game_name = argv[1]

    # create game
    adventure = Adventure(game_name)

    # welcome user
    print("Welcome to Adventure.\n")

    # print very first room description
    print(adventure.get_description())

    # prompt the user for commands until they type QUIT
    while True:

        # prompt
        command = input("> ").upper()

        # check if command entered is an abbreviation in the synonym dictionary
        if command in adventure.synonymdict:

            # change abbreviation to full command
            command = adventure.synonymdict[command]

        # if command is 'HELP', print the game instructions
        if command == "HELP":
            print("You can move by typing directions such as EAST/WEST/IN/OUT\n"
                  "QUIT quits the game\n"
                  "HELP prints instructions for the game\n"
                  "LOOK lists the complete description of the room and its contents.")

        # if command is 'LOOK', print the long description of the current room
        elif command == "LOOK":
            print(adventure.get_long_description())

        # escape route
        elif command == "QUIT":
            break

        else:
            # check if command is a possible move, if not: print invalid command
            if adventure.move(command) == False:
                print("Invalid command.")

            # check if move is forced, as if so, give discription and move
            else:
                if adventure.is_forced() == True:
                    print(adventure.get_description())
                    adventure.move("FORCED")
                print(adventure.get_description())