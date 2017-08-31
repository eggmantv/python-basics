class Enemy:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

        self.active = True

    def be_hit(self, weapon):
        self.attacked_by_weapon = weapon
        self.hp -= weapon.power

        print("{}'s hp remains {}".format(self.name, self.hp))
        if self.hp <= 0:
            self.be_killed()

        if weapon.can_explode:
            weapon.explode()

    def be_killed(self):
        print("{} is killed by {}".format(self.name, self.attacked_by_weapon.name))
        self.active = False


class Laser:

    def __init__(self, power):
        self.name = self.__class__.__name__
        self.power = power

        self.can_explode = False

class Bomb:

    def __init__(self, power):
        self.name = self.__class__.__name__
        self.power = power

        self.can_explode = True

    def explode(self):
        print('boom!')

enemy1 = Enemy('slim', 3)
enemy1.be_hit(Laser(1))
enemy1.be_hit(Laser(1))
enemy1.be_hit(Bomb(1))
