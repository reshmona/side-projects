# Robot class for 2D navigation

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
        self.direction_index = 0  # Start facing NORTH

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % 4

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % 4

    def move(self):
        direction = self.directions[self.direction_index]
        if direction == 'NORTH':
            self.y += 1
        elif direction == 'EAST':
            self.x += 1
        elif direction == 'SOUTH':
            self.y -= 1
        elif direction == 'WEST':
            self.x -= 1

    def report(self):
        return f"{self.x},{self.y},{self.directions[self.direction_index]}"
