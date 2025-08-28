from rectangular_room import RectangularRoom

class EmptyRoom(RectangularRoom):
    def is_tile_accessible(self, x, y):
        return 0 <= int(x) < self.width and 0 <= int(y) < self.height


