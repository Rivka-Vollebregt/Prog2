################################################################################
# room.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
# 28-5-2020
#
# creates room objects for the adventure game in adventure.py


class Room():

    # initialize room information like ID, name and description
    def __init__(self, room_ID, name, description):
        self.room_ID = room_ID
        self.name = name
        self.description = description

        # set room visited to False (no room has first time been visited)
        self.visited = False

        # dictionary to store the connections between rooms
        self.connections = {}

    # stores direction and room in the dictionary
    def add_connection(self, direction, room):
        self.connections[direction] = room

    # checks if there's a connection in the dictionary
    def has_connection(self, direction):
        if direction in self.connections:
            return True
        return False

    # retrieves Room object that direction is connected to
    def get_connection(self, direction):
        return self.connections[direction]

    # sets the visited parameter of the room to already visited (True)
    def set_visited(self):
        self.visited = True

    # check if a room has already been visited and returns true if so
    def already_visited(self):
        return self.visited