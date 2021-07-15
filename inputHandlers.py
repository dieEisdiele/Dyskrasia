from typing import Optional

import tcod.event

from actions import Action, BumpAction, EscapeAction



class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: "tcod.event.Quit") -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: "tcod.event.KeyDown") -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_KP_1:
            action = BumpAction(-1, 1)
        elif key == tcod.event.K_KP_2 or key == tcod.event.K_DOWN:
            action = BumpAction(0, 1)
        elif key == tcod.event.K_KP_3:
            action = BumpAction(1, 1)
        elif key == tcod.event.K_KP_4 or key == tcod.event.K_LEFT:
            action = BumpAction(-1, 0)
        elif key == tcod.event.K_KP_5 or key == tcod.event.K_SPACE:
            action = BumpAction(0, 0)
        elif key == tcod.event.K_KP_6 or key == tcod.event.K_RIGHT:
            action = BumpAction(1, 0)
        elif key == tcod.event.K_KP_7:
            action = BumpAction(-1, -1)
        elif key == tcod.event.K_KP_8 or key == tcod.event.K_UP:
            action = BumpAction(0, -1)
        elif key == tcod.event.K_KP_9:
            action = BumpAction(1, -1)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action