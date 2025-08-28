from abc import ABC, abstractmethod
import random

class Robot(ABC):
    def __init__(self, room):
        self.room = room
        self.cleaned_tiles = set()
        self.x = random.randint(0, room.width - 1)
        self.y = random.randint(0, room.height - 1)
        

    @abstractmethod
    def move(self):
        pass

    def clean_tiles(self):
        """ Clean the current tile and add it to the cleaned_tiles set"""
        self.cleaned_tiles.add((self.x, self.y))



    def coverage(self):
        """Calculate how much of the room has been cleaned"""
        total_tiles = self.room.width * self.room.height
        return len(self.cleaned_tiles) / total_tiles