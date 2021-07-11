import arcade
import random
import math

class EnemyTeam:

    def __init__(self, width, height, enemy_levels_qty:dict):
        """
        Definimos los diferentes niveles de los enemigos y la cantidad de estos
        Params enemy_levels_qty: dict
            {
                1: 10,
                2: 15,
            }
            10 enemigos de nivel 1 y 15 enemigos nivel 2
        """
        self.width = width
        self.height = height
        self.enemy_qty = sum([enemy_qty for enemy_qty in enemy_levels_qty.values()])
        self.enemies_list = [Enemy(1, 1,ene_lvl) for ene_lvl in enemy_levels_qty for n in range(enemy_levels_qty[ene_lvl])]
        self.bullet_list = arcade.SpriteList()
        self.bullet_frencuency = 60
        self.bullet_speed = 1

    def setup_enemies(self):

        for enemy_obj in self.enemies_list:
            
            # Icono de las naves enemigas.
            enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.3)
            enemy.angle = 180 

            # Posicion aleatoria de las naves enemigas
            enemy.center_x = random.randrange(self.width)
            enemy.center_y = random.randrange(300, self.height)

            # Agregar las naves enemigas
            enemy_obj.set_sprite(enemy)

    def draw_enemies(self):
        self.bullet_list.draw()
        for enemy_obj in self.enemies_list:
            enemy_obj.sprite.draw()
        
    def shoot_enemies(self, player, frame_count):

        for enemy_obj in self.enemies_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.
            enemy = enemy_obj.sprite
            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = player.center_x
            dest_y = player.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle)-90

            # Shoot every 60 frames change of shooting each frame
            # CAMBIAR LA FRECUENCIA DEL DISPARO
            if frame_count % self.bullet_frencuency == 0:
                print("Creando bala")
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * self.bullet_speed
                bullet.change_y = math.sin(angle) * self.bullet_speed

                self.bullet_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()
    
    def is_attacked(self, player_bullet_list):

        for bullet in player_bullet_list:

            for i, enemy_obj in enumerate(self.enemies_list):
                enemy = enemy_obj.sprite

                hit = arcade.check_for_collision(bullet, enemy)
                if hit:
                    bullet.remove_from_sprite_lists()
                    print("Hubo un hit")
                    enemy_obj.is_attacked()
                    if enemy_obj.is_death():
                        self.enemies_list.pop(i)

            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

    def update_enemies(self):

        self.bullet_list.update()
        for enemy_obj in self.enemies_list:
            enemy_obj.sprite.update()

class Enemy:

    def __init__(self, health, attack, nivel, sprite=None):
        self.health = health
        self.attack = attack
        self.nivel = nivel
        self.sprite = sprite
        self.current_health = health

    def get_attack(self):

        if self.nivel in [1,2]:
            return self.attack
        elif self.nivel == 3:
            return self.attack * 3

    def get_health(self):

        if self.nivel == 1:
            return self.health
        elif self.nivel == 2:
            return self.health * 3
        elif self.nivel == 3:
            return self.health * 5

    def set_sprite(self, sprite):
        
        self.sprite = sprite

    def update_sprite(self):
        
        self.sprite.update()
    
    def is_attacked(self):
        if self.current_health:
            self.current_health -= 1
    
    def is_death(self):
        if self.current_health:
            return False
        else:
            self.sprite.kill()
            return True

            