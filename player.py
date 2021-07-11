
class Player():

    def __init__(self, health, health_point, attack, score):
        # Variables fijas
        self.init_health = health
        self.init_health_point = health_point
        # Variables de juego
        self.health = health
        self.health_point = health_point
        self.attack = attack
        self.score = score

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health

    def get_health_point(self):

        return self.health_point
    
    def attacked(self):
        
        if self.health_point > 1:
            self.health_point -= 1
        
        if self.health_point == 1:
            self.health -= 1
            if self.health >= 0:
                self.health_point = self.init_health_point
            else:
                return False
        
        return self.health, self.health_point

    def death_enemy(self, enemy_level=1):

        if enemy_level == 1:
            self.score += 25
        if enemy_level == 2:
            self.score += 50
        if enemy_level == 3:
            self.score += 100


    def add_score(self, points):
        
        self.score = self.score + points
