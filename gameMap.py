from __future__ import annotations

from typing import Iterable, Optional, TYPE_CHECKING

import numpy as np   # type: ignore
from tcod.console import Console

import tileTypes

if TYPE_CHECKING:
    from entity import Entity



class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), tileTypes.wall, order="F")

        self.visible = np.full((width, height), False, order="F")   # Tiles the player can currently see
        self.explored = np.full((width, height), False, order="F")   # Tiles the player has seen before

    def getBlockingEntity(self, locationX: int, locationY: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.blocksMovement and entity.x == locationX and entity.y == locationY:
                return entity

        return None

    def inBounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
        
        If a tile is in the "visible" array, then draw it with the "light" colours.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colours.
        Otherwise, the default is "shroud".
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tileTypes.shroud
        )

        for entity in self.entities:
            # Only print entities that are in the FOV.
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, entity.colour)