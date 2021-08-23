import random
from Point import Point
from enum import Enum


class SnakeGame:
    """
    Contains game model and update_game method.
    Does not supply graphics, menu, etc.
    """

    def __init__(self, wrap=True, grid_size=Point(20, 20)):
        """
        Initialize Game State.
        :param wrap:
        :param grid_size:
        """
        self.snake = [Point(6, 10), Point(5, 10), Point(4, 10), Point(3, 10)]
        self.apple = Point(10, 3)
        self.status = GameStatus.ACTIVE

        self._grid_size = grid_size
        self._wrap = wrap
        self._direction = SnakeCommands.UP
        self._pause = False

    def update_game(self, command):
        """
        Main Update loop: Run a frame of the game.

        :param command: A command from the SnakeCommands class.
        :return: A GameStatus enum.
        """
        if command is SnakeCommands.PAUSE:
            self._pause = self._pause is False
            self.status = GameStatus.PAUSED
            return

        if self._pause:
            return

        self._set_snake_move_direction(command)
        preview_head = self._update_head()

        if self._check_crash(preview_head):
            print("Crash!!!")
            self.status = GameStatus.GAME_OVER
            return

        if self._check_eat_apple(preview_head):
            self.apple = self._spawn_apple()
        else:
            self.snake.pop()

        self.snake.insert(0, preview_head)
        self.status = GameStatus.ACTIVE

    def _spawn_apple(self):
        """
        Create an apple on the board.
        """
        return Point(
            int(random.random() * self._grid_size.x),
            int(random.random() * self._grid_size.y),
        )

    def _set_snake_move_direction(self, command):
        """
        Set the direction the snake will advance.
        Filter out invalid movements.
        :param command: A Point movement command.
        """
        if command is None:
            return

        # Check if command will reverse snake into itself. Let's help the player prevent this mis-click
        if command.x * self._direction.x < 0 or command.y * self._direction.y < 0:
            return

        self._direction = command

    def _update_head(self):
        """
        Advance the head of the snake by 1 move.
        """
        head = Point(
            self.snake[0].x + self._direction.x, self.snake[0].y + self._direction.y
        )

        if self._wrap:
            if head.x < 0:
                head.x = self._grid_size.x - 1
            if head.x >= self._grid_size.x:
                head.x = 0
            if head.y < 0:
                head.y = self._grid_size.y - 1
            if head.y >= self._grid_size.y:
                head.y = 0
        else:
            if (
                head.x < 0
                or head.x >= self._grid_size.x
                or head.y < 0
                or head.y >= self._grid_size.y
            ):
                head = self.snake[0]
        return head

    def _check_eat_apple(self, head):
        """
        Check if the snake is head is eating the apple in this move.
        :param head:
        :return:
        """
        if head == self.apple:
            return True
        return False

    def _check_crash(self, head):
        """
        Check if snake has crashed, losing the game.
        :param head: The Point that the head is at.
        :return: True if snake crashed. False if snake is still safe.
        """
        if head in self.snake:
            return True
        return False

    @property
    def grid_size(self):
        return self._grid_size


class GameStatus(Enum):
    PAUSED = 1
    ACTIVE = 2
    GAME_OVER = 3


class SnakeCommands:
    LEFT = Point(-1, 0)
    RIGHT = Point(1, 0)
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    START = "Start"
    QUIT = "Quit"
    PAUSE = "Pause"
