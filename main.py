#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from inputHandlers import EventHandler



def main() -> None:
    screenWidth = 80
    screenHeight = 50

    playerX = int(screenWidth/2)
    playerY = int(screenHeight/2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu16x16_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    eventHandler = EventHandler()

    with tcod.context.new_terminal(
        screenWidth,
        screenHeight,
        tileset=tileset,
        title="Dyskrasia",
        vsync=False,
    ) as context:
        rootConsole = tcod.Console(screenWidth, screenHeight, order="F")
        while True:
            rootConsole.print(x=playerX, y=playerY, string="@")

            context.present(rootConsole)

            rootConsole.clear()

            for event in tcod.event.wait():
                action = eventHandler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    playerX += action.dx
                    playerY += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit



if __name__ == "__main__":
    main()