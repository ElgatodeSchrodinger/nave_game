

# In[1]:
#Menu del juego e instrucciones de "Space Dome"

import arcade
import os

file_path = os.path.dirname(os.path.abspath("__file__"))
os.chdir(file_path)
 #Dimensiones graficas de la pantalla del menu 
SCALE = 0.5
OFFSCREEN_SPACE = 500
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Space Dom"
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE
 
#Clase del menu inicial.
class menu(arcade.View):
    #Fondo de pantalla
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

    #Formato de letras
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("SPACE DOME", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Clic para continuar", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
    #Funciones del mouse
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = Instrucciones()
        self.window.show_view(instructions_view)
 
 
class Instrucciones(arcade.View):
    #Fondo de pantalla de las intrucciones del juego
     def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
     #Formato del texto
     def on_draw(self):
         arcade.start_render()
         arcade.draw_text("El Planeta esta siendo atacado por naves de la galaxia Pythomeda. ¡Destruyelos y salva La Tierra!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                          arcade.color.WHITE, font_size=15, anchor_x="center")
         arcade.draw_text("Comenzar el juego", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                          arcade.color.LIGHT_GRAY, font_size=20, anchor_x="center")
     #Funciones del mouse
     def on_mouse_press(self, _x, _y, _button, _modifiers):
         game_view = GameView()
         self.window.show_view(game_view)
 
 #Visor
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        #os.system('python -m proyecto.codigos.juego')
        
        
        
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Space Dome")
    window.total_score = 0
    ver_menu= menu()
    window.show_view(ver_menu)
    arcade.run()


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




