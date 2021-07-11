#Juego Space Dome.
#Desarrollado por: Pablo Aranda, Catalina Cabrera, Carlos Figueroa, Renato Riquelme y Javier Valenzuela.

import arcade
import random
import math
import os

#Dimensiones graficas de la pantalla de juego
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Dome"
BULLET_SPEED = 4
HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25

dirname = os.path.dirname(__file__)

#Clase principal del juego.
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Inicializacion.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        # Variables contenidas para los disparos.
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.enemy_list = None

        # Informacion del jugador en pantalla.
        self.player_sprite = None
        self.score = 0

        # Sonidos de los disparos
        self.gun_sound = arcade.sound.load_sound("sounds/laser_shot.wav")
        self.hit_sound = arcade.sound.load_sound("sounds/explosion.wav")
        
        #Color de fondo del juego.
        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

    def setup(self):

        #Musica de fondo del juego
        self.background_music = arcade.load_sound(
            os.path.join(dirname,"sounds/explosion.wav"))
            
        # Sprites
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        #Contador del jugador
        self.score = 0

        # Imagen de la nave del jugador.
        self.player_sprite = arcade.Sprite(os.path.join(dirname,"images/self_ship.png"), SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Creacion de las naves enemigas (estaticas por el momento)
        for coin_index in range(COIN_COUNT):

            # Icono de las naves enemigas.
            coin = arcade.Sprite("images/enemy_ship.png", SPRITE_SCALING_COIN)
            coin.angle = 180 

            # Posicion aleatoria de las naves enemigas
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(150, SCREEN_HEIGHT)

            # Agregar las naves enemigas
            self.coin_list.append(coin)

   
        
        arcade.sound.play_sound(self.gun_sound)

        # Imagen de los disparos
        bullet = arcade.Sprite("images/laser.png", SPRITE_SCALING_LASER)
    
    def on_draw(self):
        
        arcade.start_render()
        
        self.player_list.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.explosions_list.draw()
        
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.White,14)
  
    def on_mouse_motion(self, x, y, dx, dy):
        
        self.player_sprite.center_x = x
    
    def on_mouse_press(self, x, y, button , modifiers):
        
        # Sonido que se ejecutara al percutar la bala 
        arcade.play_sound(self.gun_sound)
        # Aspecto de la bala
        bullet = arcade.Sprite("images/laser.png", SPRITE_SCALING_LASER)

        
        bullet.angle = 90

    
        bullet.change_y = BULLET_SPEED

        # Posicion de la bala
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        self.bullet_list.append(bullet)

    def on_update(self, delta_time):

        self.frame_count += 1

    #Loop para disparos teledirigidos al jugador por parte de las naves.
        for enemy in self.enemy_list:

            #Se calcula el angulo y posicion para enviar la bala
            start_x = enemy.center_x
            start_y = enemy.center_y

            
            dest_x = self.player.center_x
            dest_y = self.player.center_y

            #Se calcula en angulo en radianes el destino de la bala
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Se selecciona el enemigo
            enemy.angle = math.degrees(angle)-90

            bullet = arcade.Sprite("images/laser.png", SPRITE_SCALING_LASER)

            # Los disparos se ejecutan cada 60 frames
            bullet.center_x = start_x
            bullet.center_y = start_y

        
            bullet.angle = math.degrees(angle)

            #Velocidad de la bala
            bullet.change_x = math.cos(angle) * BULLET_SPEED
            bullet.change_y = math.sin(angle) * BULLET_SPEED

            self.bullet_list.append(bullet)

        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    
        self.bullet_list.update()
        self.explosions_list.update()

        #Bala cuando impacta la nave
    #(pablo 28/6)
        for bullet in self.bullet_list:
            
            hit_list = arcade.check_for_coallision_with_list(bullet, self.coin_list)
        
            if len(hits_list) > 0:
                
                bullet.remove_form_sprite_lists
        
            if coin in hit_list:
            
                for i in range(PARTICLE_COUNT):
                    particle = Particle(self.explosions_list)
                    particle.position = coin.position
                    self.explosions_list.append(particle)
            
                smoke = Smoke(50)
                smoke.position = coin.position
                self.explosions_list.append(smoke)
            
                coin.remove_form_sprite_lists()
                self.score += 1
            
                arcade.sound.play_sound(self.hit_sound)
        
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_form_sprite_lists()
#Movimientos y logioca del juego
    
        for bullet in self.bullet_list:

            # Cuando la bala impacta la nave
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

        #Si impacta, se deshace la bala
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # El proceso cuando la bala impacta la nave
            for coin in hit_list:
                # La nave pierde una vida
                coin.cur_health -= 1

                # Chequear las vidas de las naves
                if coin.cur_health <= 0:
                    # Si llega a 0 las vidas, muere
                    coin.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.death_sound)
                else:
                    # No muere, solo le impacta
                    arcade.play_sound(self.hit_sound)

            # Cuando las balas salen de la pantalla, desaparece.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

#Clase sobre la vida que tienen los enemigos
class SpriteWithHealth(arcade.Sprite):
   

    def _init_(self, image, scale, max_health):
        super()._init_(image, scale)

        
        self.max_health = max_health
        self.cur_health = max_health

    def draw_health_number(self):
      

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=self.center_x + HEALTH_NUMBER_OFFSET_X,
                         start_y=self.center_y + HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)

#Funcion que muestra el estado de la vida de las naves.
    def draw_health_bar(self):
        

        #Cuando pierde vidas: self.cur_health < self.max_health:
        arcade.draw_rectangle_filled(center_x=self.center_x,
                                        center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                                        width=HEALTHBAR_WIDTH,
                                        height=3,
                                        color=arcade.color.RED)

        
        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.center_x - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.center_y - 10,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)




#Modulo que hace correr el juego.
def main():
    
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()