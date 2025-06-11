import sdl2
from window import Window

def render(window: Window):
    sdl2.SDL_SetRenderDrawColor(window.renderer, 0, 0, 0, 255)
    sdl2.SDL_RenderClear(window.renderer)

    # Rita här
    sdl2.SDL_SetRenderDrawColor(window.renderer, 0, 255, 0, 255)
    sdl2.SDL_RenderDrawLine(window.renderer, 50, 50, 200, 50)

    sdl2.SDL_RenderPresent(window.renderer)