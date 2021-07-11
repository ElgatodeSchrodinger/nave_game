"""
Show how to have enemies shoot bullets aimed at the player.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_bullets_enemy_aims
"""

import arcade
import math
import os
import random
from enemy import Enemy, EnemyTeam
from player import Player

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprites and Bullets Enemy Aims Example"
BULLET_SPEED = 1


class MyGame(arcade.Window):
    """ Main application class """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

        self.enemy_list = None
        self.bullet_list = None
        self.player_bullet_list = None
        self.player_list = None
        self.player = None

        self.player_obj = Player(3, 3, 1, 0)
                
        self.enemy_team = EnemyTeam(SCREEN_WIDTH, SCREEN_HEIGHT, {1:5, 2:5})

    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Add player ship
        self.player = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.3)
        self.player_list.append(self.player)

        self.enemy_team.setup_enemies()

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_bullet_list.draw()
        self.player_list.draw()

        self.enemy_team.draw_enemies()

    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        # Loop through each enemy that we have
        # UPDATE ENEMIES
        self.enemy_team.shoot_enemies(self.player, self.frame_count)

        for bullet in self.player_bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.enemy_team.is_attacked(self.player_bullet_list)
        
        self.enemy_team.update_enemies()
        
        self.player_bullet_list.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Gunshot sound
        # arcade.sound.play_sound(self.gun_sound)

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", 0.8)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90

        # Give it a speed
        bullet.change_y = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player.center_x
        bullet.bottom = self.player.top

        # Add the bullet to the appropriate lists
        self.player_bullet_list.append(bullet)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
