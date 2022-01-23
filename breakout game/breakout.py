"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.

This program plays a game called "break out" in which players
moving the paddle to make the ball bounce and break all bricks!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1500 / 120 # 120 frames per second
NUM_LIVES = 3			# The number of lives


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    dx = graphics.get_x_velocity()
    dy = graphics.get_y_velocity()

    while True:
        life = graphics.life
        total_score = graphics.score
        pause(FRAME_RATE)
        if graphics.switch and life > 0:
            graphics.ball.move(dx, dy)
            a = graphics.maybe()
            if a is graphics.life_label or a is graphics.score_label:
                graphics.reset_ball_position()
                graphics.lose_one_life()
                graphics.switch = False
            elif a is not graphics.paddle and a is not graphics.life_label and a is not graphics.score_label and a is not None:
                graphics.window.remove(a)
                total_score = graphics.count_score()
                dy = -dy
            elif a is not None:
                if dy > 0:
                    dy = -dy
            elif graphics.ball.y <= 0:
                dy = -dy
            elif graphics.ball.x <= 0 or graphics.ball.x + graphics.ball_radius*2 >= graphics.window_width:
                dx = -dx
            elif graphics.ball.y + graphics.ball.height >= graphics.window_height:
                graphics.reset_ball_position()
                graphics.lose_one_life()
                graphics.switch = False
            elif total_score == graphics.brick_rows * graphics.brick_rows:
                graphics.show_win_label()
                break


if __name__ == '__main__':
    main()
