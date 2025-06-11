import sdl2
import ctypes

from window import Window
from input import *
from render import render

class App:
    def __init__(self, window_title: str="Fönster", window_width: int=600, window_height: int=400):
        # Startar SDL:
        if sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING != 0):
            print(f"ERROR::SDL::Kunde inte starta SDL: {sdl2.SDL_GetError()}")

        # Fönstret/Renderern:
        self.window = Window(window_title, window_width, window_height)
        if self.window is None:
            print(f"ERROR::SDL::Fönstret kunde inte skapas: {sdl2.SDL_GetError()}")

    def run_app(self):
        game_runnig = True

        # Fönstrets storlek: ------------------------
        window_width = ctypes.c_int()
        window_height = ctypes.c_int()
        sdl2.SDL_GetWindowSize(self.window.sdl_window, ctypes.byref(window_width), ctypes.byref(window_height))

        last_window_width = ctypes.c_int()
        last_window_height = ctypes.c_int()
        # --------------------------------------------

        while (game_runnig):
            # Fönstrets storlek: ------------------------
            sdl2.SDL_GetWindowSize(self.window.sdl_window, ctypes.byref(window_width), ctypes.byref(window_height))
            if last_window_width.value != window_width.value or last_window_height.value != window_height.value:
                print(f"x: {window_width}, y: {window_height}")

            last_window_width.value = window_width.value
            last_window_height.value = window_height.value
            # --------------------------------------------

            game_runnig = process_input() # Input
            render(self.window) # Render
            # TODO! update

    def __del__(self):
        sdl2.SDL_Quit()

def main():
    application = App("spel", 600, 400)
    application.run_app()

if __name__ == "__main__":
    main()