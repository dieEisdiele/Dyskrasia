#!/usr/bin/env python3
import copy

import tcod

from engine import Engine
import entityFactories
from inputHandlers import EventHandler
from procgen import generateDungeon



def main() -> None:
    screenWidth = 80
    screenHeight = 50

    mapWidth = 80
    mapHeight = 45

    roomMaxSize = 10
    roomMinSize = 6
    maxRooms = 30

    maxEnemiesPerRoom = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    eventHandler = EventHandler()

    player = copy.deepcopy(entityFactories.player)

    gameMap = generateDungeon(
        maxRooms,
        roomMinSize,
        roomMaxSize,
        mapWidth,
        mapHeight,
        maxEnemiesPerRoom,
        player
    )

    engine = Engine(eventHandler, gameMap, player)

    with tcod.context.new_terminal(
        screenWidth,
        screenHeight,
        tileset=tileset,
        title="Dyskrasia",
        vsync=False,
    ) as context:
        rootConsole = tcod.Console(screenWidth, screenHeight, "F")
        while True:
            engine.render(rootConsole, context)

            events = tcod.event.wait()

            engine.handleEvents(events)



if __name__ == "__main__":
    main()