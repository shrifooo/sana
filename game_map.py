import numpy as np
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self , width:int , height:int) -> None:
        self.width = width
        self.height = height
        self.tiles = np.full((width , height) , fill_value=tile_types.floor , order="F")

        self.tiles[30:33 , 22] = tile_types.wall

    def in_bounds(self , x:int , y:int)-> bool:
        if(x in range(0 , self.width+1) and y in range(0 , self.height + 1)):
            return True
        else:
            return False
        
    def render(self , console:Console)->None:
        console.tiles_rgb[0:self.width ,0:self.height] = self.tiles["dark"]
