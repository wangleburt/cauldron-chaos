import pygame

MOUSE_NONE = 0
MOUSE_LEFT = 1
MOUSE_RIGHT = 2

def init():
    pygame.display.set_mode((100,100))
    return

def didClickMouse():
    events = pygame.event.get(pygame.MOUSEBUTTONUP)
    pygame.event.get() # clears other events out of event queue
    return (len(events) > 0)

def clickType():
    events = pygame.event.get(pygame.MOUSEBUTTONUP)
    pygame.event.get() # clears other events out of event queue
    if len(events) > 0:
        event = events[0]
        if event.button == 1:
            return MOUSE_LEFT
        else:
            return MOUSE_RIGHT
    else:
        return MOUSE_NONE

# tell the system that we're still listening for events, don't assume we froze
def idle():
    pygame.event.pump()
    return

def clear():
    pygame.event.clear()
    return
    