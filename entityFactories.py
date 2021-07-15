from entity import Entity



player = Entity(char="@", colour=(255, 255, 255), name="Player", blocksMovement=True)

guard = Entity(char="G", colour=(180, 0, 0), name="Guard", blocksMovement=True)
plagueDoctor = Entity(char="P", colour=(0, 0, 0), name="Plague Doctor", blocksMovement=True)