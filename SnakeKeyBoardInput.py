import pygame
from SnakeGame import SnakeCommands


class SnakeKeyBoardInput:
    """
    This class maps keyboard input into snake commands.
    """

    def __init__(self, verbose=True):
        """
        Convert pygame inputs to commands specific to SnakeGame
        :param verbose: Prints out command input to console.
        """
        self.command = SnakeCommands.RIGHT
        self.verbose = verbose

    def get_command(self):
        """
        Returns SnakeGame command, using keyboard input.
        Although this method is essentially a map, debugging is much easier when
        it is easy to break on specific commands, thus the implementation with if statements.
        :return: Selected command
        """

        # Disable linting violations (these members do exist, but linter does not recognize them)
        # pylint: disable=no-member
        for event in pygame.event.get():
            command = None

            # BUG: Possible bug in pygame?
            # pygame.QUIT == 256, but the exit (X button in corner of window throws event = 32768)
            X_BUTTON_CLICKED = 32787
            if event.type == X_BUTTON_CLICKED:
                command_str = "Quit"
                command = SnakeCommands.QUIT

            keys = pygame.key.get_pressed()
            pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                command_str = "Left"
                command = SnakeCommands.LEFT

            if keys[pygame.K_RIGHT]:
                command_str = "Right"
                command = SnakeCommands.RIGHT

            if keys[pygame.K_UP]:
                command_str = "Up"
                command = SnakeCommands.UP

            if keys[pygame.K_DOWN]:
                command_str = "Down"
                command = SnakeCommands.DOWN

            if keys[pygame.K_p]:
                command_str = "Pause"
                command = SnakeCommands.PAUSE

            if keys[pygame.K_RETURN]:
                command_str = "Start"
                command = SnakeCommands.START

            if keys[pygame.K_END]:
                command_str = "Quit"
                command = SnakeCommands.QUIT

            if command is not None and self.verbose:
                print("Command: %r" % command_str)

            return command
