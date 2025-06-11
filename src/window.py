import sdl2
import ctypes

class Window:
    def __init__(self, title: str="Fönster", window_width: int=600, window_height: int=400):
        self.window_title = title
        self.window_width = window_width
        self.window_height = window_height

        # Fönstret:
        self.window_title = ctypes.c_char_p(self.window_title.encode("utf-8"))

        self.sdl_window = sdl2.SDL_CreateWindow(
            self.window_title,
            sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED,
            self.window_width, self.window_height,
            sdl2.SDL_WINDOW_RESIZABLE
        )

        if self.sdl_window is None:
            print(f"ERROR::Kunde inte skapa fönstret: {sdl2.SDL_GetError()}")

        # Rendern:
        self.renderer = sdl2.SDL_CreateRenderer(
            self.sdl_window,
            -1,
            sdl2.SDL_RENDERER_PRESENTVSYNC | sdl2.SDL_RENDERER_ACCELERATED
        )

        if self.renderer is None:
            print(f"ERROR::Kunde inte skapa renderern: {sdl2.SDL_GetError()}")