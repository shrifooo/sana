from __future__ import annotations
import tcod

from engine import Engine 
from input_handlers import EventHandler
from entity import Entity
from game_map import GameMap

def main()->None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    player_x = int(screen_width/2)
    player_y = int(screen_height/2) 


    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png" , 32 , 8 , tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(x=player_x, y=player_y, char="@" , color = (255 , 255 , 255))
    npc = Entity(x=player_x, y=player_y, char="N" , color = (255 , 255 , 0))
    entities = {player , npc}

    game_map = GameMap(width=map_width , height=map_height)

    engine = Engine(entities=entities , event_handler= event_handler ,game_map = game_map ,player=player)

    with tcod.context.new_terminal(
        columns = screen_width,
        rows = screen_height,
        tileset = tileset,
        title = "Sana",
        vsync = True,
    ) as context:
        root_console = tcod.console.Console(screen_width , screen_height , order = "F")
        while True:
            
            root_console.clear()

            engine.render(console = root_console , context = context)

            events = tcod.event.wait()

            engine.handle_events(events)


                


if __name__ == "__main__":
    main()