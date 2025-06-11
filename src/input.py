import sdl2
import ctypes
from sdl2 import SDL_PollEvent

event = sdl2.SDL_Event()

def process_input() -> bool:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            return False

    return True