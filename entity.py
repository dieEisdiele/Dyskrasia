from __future__ import annotations

import copy
from typing import Tuple
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from gameMap import GameMap

T = TypeVar("T", bound="Entity")



class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        char:str = "?",
        colour: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        blocksMovement: bool = False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.colour = colour
        self.name = name
        self.blocksMovement = blocksMovement

    def spawn(self: T, gameMap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gameMap.entities.add(clone)
        return clone

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy