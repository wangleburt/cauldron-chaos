import pygame

def init():
    pygame.display.set_mode((100,100))
    return

def didClickMouse():
    events = pygame.event.get(pygame.MOUSEBUTTONUP)
    pygame.event.get() # clears other events out of event queue
    return (len(events) > 0)

# tell the system that we're still listening for events, don't assume we froze
def idle():
    pygame.event.pump()
    return

def clear():
    pygame.event.clear()
    return
    