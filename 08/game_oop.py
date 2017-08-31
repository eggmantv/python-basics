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


class Weapon:

    def __init__(self, power, can_explode):
        self.name = self.__class__.__name__
        self.power = power

        self.can_explode = can_explode

    def be_destroyed(self):
        print("{} was destroyed".format(self.name))


class Laser(Weapon):

    def __init__(self, power):
        super().__init__(power, False)


class Bomb(Weapon):

    def __init__(self, power):
        super().__init__(power, True)

    def explode(self):
        print('boom!')
        self.be_destroyed()


def game_start():
    enemy1 = Enemy('slim', 3)
    enemy1.be_hit(Laser(1))
    enemy1.be_hit(Laser(1))
    enemy1.be_hit(Bomb(1))


if __name__ == '__main__':
    game_start()
