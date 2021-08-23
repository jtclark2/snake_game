import pygame


class BoardDisplay:
    """(View) Displays board to screen."""

    BLUE = (0, 0, 128)
    GREEN = (0, 128, 0)
    RED = (255, 0, 0)
    GREY = (128, 128, 128)
    BLACK = (0, 0, 0)

    def __init__(self, grid_size):

        self.grid_size = grid_size

        # Create Window
        self.window_width_pixels = 500
        self.window_height_pixels = 500
        self.window = pygame.display.set_mode(
            (self.window_width_pixels, self.window_height_pixels)
        )

        # Setup Grid
        self.box_width = self.window_width_pixels // self.grid_size.x
        self.box_height = self.window_height_pixels // self.grid_size.y

        self.background_color = BoardDisplay.BLACK
        self.line_color = BoardDisplay.GREY
        self.grid_line_width = 1
        self.draw_board()

        pygame.display.update()

    def draw_board(self):
        x = 0
        y = 0
        self.window.fill(self.background_color)
        for vertical_line in range(self.grid_size.x):
            x = (vertical_line + 1) * self.box_width
            pygame.draw.line(
                self.window,
                self.line_color,
                (x, 0),
                (x, self.window_width_pixels),
                self.grid_line_width,
            )

        for horizontal_line in range(self.grid_size.y):
            y = (horizontal_line + 1) * self.box_height
            pygame.draw.line(
                self.window,
                self.line_color,
                (0, y),
                (self.window_height_pixels, y),
                self.grid_line_width,
            )

    def draw_box(self, point, color):
        pygame.draw.rect(
            self.window,
            color,
            (
                point.x * self.box_width + self.grid_line_width,
                point.y * self.box_height + self.grid_line_width,
                self.box_width - self.grid_line_width,
                self.box_height - self.grid_line_width,
            ),
        )

    def draw_boxes(self, points, color):
        for index, point in enumerate(points):
            if index == 0:
                self.draw_box(point, BoardDisplay.BLUE)  # Prettier snake head
            else:
                self.draw_box(point, color)

    def display_text(self, text):
        pygame.font.init()
        try:
            font = pygame.font.Font(
                pygame.font.get_default_font(), 32
            )  # There's probably a font list somewhere?
            # font = pygame.font.Font('freesansbold.ttf', 32) # There's probably a font list somewhere?
            text_background_color = BoardDisplay.BLUE
            text_render = font.render(
                text, True, BoardDisplay.GREEN, text_background_color
            )

            text_rect = text_render.get_rect()
            text_rect.center = (
                self.window_width_pixels // 2,
                self.window_height_pixels // 2,
            )

            self.window.blit(text_render, text_rect)
        except TypeError:
            # When building the .exe, the fonts aren't building correctly.
            # I would guess that the .ttf file is seen as a different resource, but it's not worth fixing here

            # Pause will start work, but without the message. It's poor UX, but it isn't worth investing in now
            pass
