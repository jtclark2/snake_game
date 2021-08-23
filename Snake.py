from Point import Point
import SnakeGame


class Snake:
    """
    Contains game model and update_game method.
    Does not supply graphics, menu, etc.
    """

    def __init__(self, wrap=True, grid_size=Point(20, 20)):
        self.snake = [Point(6, 10), Point(5, 10), Point(4, 10), Point(3, 10)]
        self.apple = Point(10, 3)
        self.status = SnakeGame.GameStatus.ACTIVE

        self._grid_size = grid_size
        self._wrap = wrap
        self._direction = SnakeGame.SnakeCommands.UP
        self._pause = False

    def update_game(self, command):
        """
        Main Update loop: Run a frame of the game.

        :param command: A command from the SnakeCommands class.
        :return: A GameStatus enum.
        """
        raise NotImplementedError

    def _spawn_apple(self):
        """
        Create an apple on the board.
        """
        raise NotImplementedError

    def _set_snake_move_direction(self, command):
        """
        Set the direction the snake will advance.
        Filter out invalid movements.
        :param command: A Point movement command.
        """
        raise NotImplementedError

    def _update_head(self):
        """
        Advance the head of the snake by 1 move.
        """
        raise NotImplementedError

    def _check_eat_apple(self, head):
        """
        Check if the snake is head is eating the apple in this move.
        :param head:
        :return:
        """
        raise NotImplementedError

    def _check_crash(self, head):
        """
        Check if snake has crashed, losing the game.
        :param head: The Point that the head is at.
        :return: True if snake crashed. False if snake is still safe.
        """
        raise NotImplementedError
