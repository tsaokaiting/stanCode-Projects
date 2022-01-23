"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao

This program plays a game called "break out" in which players
moving the paddle to make the ball bounce and break all bricks!
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-ball_radius*2)/2, y=(self.window_height-ball_radius*2)/2)

        # Draw bricks
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                x = j * (brick_width+brick_spacing)
                y = i * (brick_height+brick_spacing)
                if i < 1/5 * (brick_cols):
                    self.brick.fill_color = 'red'
                elif i < 2/5 * (brick_cols):
                    self.brick.fill_color = 'orange'
                elif i < 3/5 * (brick_cols):
                    self.brick.fill_color = 'yellow'
                elif i < 4/5 * (brick_cols):
                    self.brick.fill_color = 'green'
                elif i < 5/5 * (brick_cols):
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x, y)

        # Initialize our mouse listeners
        self.switch = False
        onmouseclicked(self.startgame)
        onmousemoved(self.reset_paddle_position)

        # Default initial velocity for the ball
        self._dy = 0
        self._dx = 0
        self.set_ball_velocity()

        # Count Life remaining
        self.life = 3
        self.life_label = GLabel('Life Remaining: '+str(self.life))
        self.life_label.font = '-12'
        self.window.add(self.life_label, self.window_width-self.life_label.width, self.window_height)

        # Count the score
        self.score = 0
        self.score_label = GLabel('Score: '+str(self.score))
        self.score_label.font = '-12'
        self.window.add(self.score_label, 0, self.window_height)

        # Win the game
        self.win_label = GLabel('WIN!')
        self.win_label.color = 'red'
        self.win_label.font = '-20'

    def show_win_label(self):
        """
        When the users clear all bricks, the program will show word "WIN!"
        """
        self.window.add(self.win_label, (self.window_width-self.ball_radius*2)/2, (self.window_height-self.ball_radius*2)/2)

    def count_score(self):
        """
        When the ball collides and removes one brick, the score will be plus one.
        """
        self.score += 1
        self.score_label.text = 'Score: '+str(self.score)

    def lose_one_life(self):
        """
        When the ball falls and drops out of the window,
        the game is over and the user will lose one game life.
        """
        self.life -= 1
        self.life_label.text = 'Life Remaining: '+str(self.life)

    def startgame(self, event):
        """
        When the users click the mouse, they can start play the game.
        :param event: mouse information
        """
        if not self.switch:
            self.switch = True

    def reset_paddle_position(self, mouse):
        """
        The users use the mouse to control paddle.
        :param mouse: mouse information.
        """
        if mouse.x - self.paddle.width / 2 <= 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width / 2 >= self.window.width - self.paddle.width:
            self.paddle.x = self.window_width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def set_ball_velocity(self):
        """
        Set the velocity of the ball.
        """
        self._dx = random.randint(0, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = -self._dx
        if random.random() > 0.5:
            self._dy = -self._dy

    # Getter
    def get_x_velocity(self):
        return self._dx

    # Getter
    def get_y_velocity(self):
        return self._dy

    def maybe(self):
        """
        The four vertex of the ball.
        """
        for i in range(int(self.ball.x), int(self.ball.x)+self.ball_radius*4, self.ball_radius*2):
            for j in range(int(self.ball.y), int(self.ball.y)+self.ball_radius*4, self.ball_radius*2):
                a = self.window.get_object_at(i, j)
                if a is not None:
                    return a

    def reset_ball_position(self):
        """
        When game is over, the program will put the ball back to the original place.
        """
        self.window.add(self.ball, x=(self.window_width - self.ball_radius * 2) / 2,
                        y=(self.window_height - self.ball_radius * 2) / 2)

