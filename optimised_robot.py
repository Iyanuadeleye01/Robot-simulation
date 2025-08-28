from robot import Robot
import random

class OptimisedRobot(Robot):
    def move(self):
        """To move to the nearest uncleaned tile if possible"""
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in directions:
            new_x, new_y = self.x + dx, self.y + dy
            if self.room.is_tile_accessible(new_x, new_y) and (new_x, new_y) not in self.cleaned_tiles:
                self.x, self.y = new_x, new_y
                self.clean_tiles()
                return
            
        """Fallback to random if no uncleaned neigbors"""
        dx, dy = random.choice(directions)
        new_x, new_y = self.x + dx, self.y + dy
        if self.room.is_tile_accessible(new_x, new_y):
            self.x, self.y = new_x, new_y
        self.clean_tiles()