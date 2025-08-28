from rectangular_room import RectangularRoom

class FurnishedRoom(RectangularRoom):
    def __init__(self, width, height, dirt_amount, furniture):
        super().__init__(width, height, dirt_amount)
        self.furniture = furniture

    def is_tile_accessible(self, x, y):
        return (0 <= int(x) < self.width 
                and 0 <= int(y) < self.height
                 and int(x), int(y)) not in self.furniture
