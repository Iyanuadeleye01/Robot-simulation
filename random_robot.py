from robot import Robot
import random


class RandomRobot(Robot):
    def move(self):
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        new_x, new_y = self.x + dx, self.y + dy
        if self.room.is_tile_accessible(new_x, new_y):
            self.x, self.y = new_x, new_y

        self.clean_tiles()
