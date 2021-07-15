from typing import Tuple

import numpy as np   # type: ignore



# Tile graphics structured type compatible with Console.tiles_rgb
graphicDt = np.dtype(
    [
        ("ch", np.int32),   # Unicode codepoint
        ("fg", "3B"),   # 3 unsigned bytes, for RGB colours
        ("bg", "3B"),
    ]
)

# Tile struct used for statiscally defined tile data
tileDt = np.dtype(
    [
        ("walkable", np.bool),   # True if this tile can be walked over
        ("transparent", np.bool),   # True if this tile doesn't block FOV
        ("dark", graphicDt),   # Graphics for when this tile is not in FOV
        ("light", graphicDt),   # Graphics for when the tile is in FOV
    ]
)

def newTile(
    *,   # Enforce the use of keywords, so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), tileDt)



# shroud represents unexplored, unseen tiles
shroud = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), graphicDt)

floor = newTile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (150, 150, 150), (40, 40, 40)),
    light=(ord("."), (200, 200, 200), (200, 150, 60)),
)
wall = newTile(
    walkable=False,
    transparent=False,
    dark=(ord("▒"), (20, 20, 20), (40, 40, 40)),
    light=(ord("░"), (180, 50, 0), (100, 50, 0)),
)