from abc import ABC, abstractmethod

class RectangularRoom(ABC):

    def __init__(self, width, height,dirt_amount):
        self.width = width
        self.height = height
        # Each tile starts with the same dirt amount
        self.tiles = [[dirt_amount for _ in range(height)] for _ in range(width)]
    @abstractmethod
    def is_tile_accessible(self):
        """Return true if robot can access the tile"""
        pass
    def clean_tile_at(self, x, y, capacity):
        """ Clean the tile by robot's capacity (minimum 0 dirt)"""
        if self.tiles[int(x)][int(y)] > 0:
            self.tiles[int(x)][int(y)] = max(0, self.tiles[int(x)][int(y)] - capacity)
    
    def is_clean(self):
        """Return True if all tiles are clean"""
        return all(dirt == 0 for row in self.tiles for dirt in row)
    
    def get_num_tiles(self):
        """Return total number of tiles in the room"""
        return self.width * self.height

    def get_num_cleaned_tiles(self):
        """Return number of tiles that are completely clean"""
        return sum(1 for row in self.tiles for dirt in row if dirt == 0)