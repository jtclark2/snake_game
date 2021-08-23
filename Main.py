import pygame
from SnakeKeyBoardInput import SnakeKeyBoardInput
from GridGraphics import BoardDisplay
import SnakeGame
import time


def main():
    # The linter has difficulty recognizing pygame.init()
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member

    load_game = True
    high_score = 0
    command = None
    time_between_frames = 0.1  # seconds
    last_frame_time = time.time()

    while True:
        # Initialize game, player, and board
        if load_game:
            load_game = False
            controller = SnakeKeyBoardInput()
            # game_state = Snake.Snake(controller)
            game_state = SnakeGame.SnakeGame(controller)
            board = BoardDisplay(game_state.grid_size)

        # Main game loop
        while (
            game_state.status == SnakeGame.GameStatus.ACTIVE
            or game_state.status == SnakeGame.GameStatus.PAUSED
        ):
            now = time.time()

            possible_command = controller.get_command()
            if (
                possible_command is not None
                and possible_command is not SnakeGame.SnakeCommands.START
                and possible_command is not SnakeGame.SnakeCommands.QUIT
            ):
                command = possible_command
            else:
                if possible_command is SnakeGame.SnakeCommands.START:
                    pass  # Don't want to risk rest during game
                if possible_command is SnakeGame.SnakeCommands.QUIT:
                    break

            if now < last_frame_time + time_between_frames:
                continue
            last_frame_time = now

            game_state.update_game(command)

            # Draw
            board.draw_board()  # wipe the previous graphics
            if game_state.status == SnakeGame.GameStatus.ACTIVE:
                board.draw_box(game_state.apple, BoardDisplay.RED)
                board.draw_boxes(game_state.snake, BoardDisplay.GREEN)

            if game_state.status == SnakeGame.GameStatus.PAUSED:
                text = "Game paused."
                board.display_text(text)

            pygame.display.update()
            command = None

        else:  # Player dies this frame
            score = len(game_state.snake)
            text = "Snake died at length: %d" % score
            board.display_text(text)
            pygame.display.update()

            high_score = max(high_score, score)
            pygame.display.set_caption("High Score: %d" % high_score)

        # player is dead - viewing score overlay
        if possible_command is not None:
            menu_command = possible_command
            possible_command = None
        else:
            menu_command = controller.get_command()

        if isinstance(menu_command, str):
            if menu_command == SnakeGame.SnakeCommands.START:
                load_game = True
            if menu_command == SnakeGame.SnakeCommands.QUIT:
                break


def logger(application):
    """
    Lightweight wrapper, that saves logfiles.
    Just diverts stack trace trace to log, because the stdout is hard to see
    once application is build into an .exe
    """
    # Exception Test
    import traceback, sys  # os

    # raise(Exception("Exception on line 3"))
    try:
        application()
    except Exception as exception_instance:
        # Just log one file...this is super-lightweight, and prints the last traceback
        # Saves only the last one, so no timestamps, etc. to deal with
        # os.makedirs("Logs")
        log_file = "ErrorLog.txt"
        with open(log_file, "w", encoding="utf-8") as writer:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(f"*** Overwriting log file: {log_file}")
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=writer)

        # print("*** extract_tb to variable:")
        # var = repr(traceback.extract_tb(exc_traceback))
        # print(var)
        raise (exception_instance)


if __name__ == "__main__":
    logger(main)
