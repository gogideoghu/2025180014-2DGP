"""Objects owned by the current game scene.

Layer 0 is for background objects and layer 1 is for actors/projectiles.
"""

BACKGROUND_LAYER = 0
FOREGROUND_LAYER = 1

world = [[], []]

def add_object(o, depth=FOREGROUND_LAYER):
    """Add one object to a drawing/update layer."""
    world[depth].append(o)

def add_objects(objects, depth=FOREGROUND_LAYER):
    """Add several objects to a drawing/update layer."""
    world[depth] += objects

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot remove an object that is not in the game world')


def update():
    for layer in world:
        # An object may remove itself while updating (for example, a ball
        # that has gone outside the canvas), so iterate over a shallow copy.
        for o in list(layer):
            o.update()

def render():
    for layer in world:
        for o in list(layer):
            o.draw()


