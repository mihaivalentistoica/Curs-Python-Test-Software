class Enemy:
    def __init__(self, name):
        self.name = name
        self.lives = 1
        self.attack = 1

    def is_alive(self):
        return self.lives > 0

    def notify_if_dead(self):
        if not self.is_alive():
            return f"{self.name} lost!"

    def attack_player(self, player):
        assert isinstance(player, Player)
        return player.receive_damage(self.attack)

    def receive_damage(self, damage):
        self.lives -= damage
        return self.notify_if_dead()


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.attack = 1
        self.__position_xy = (0, 0)

    @property
    def position_xy(self):
        return self.__position_xy

    def pretty_position(self):
        x, y = self.__position_xy
        return f"{self.name} went {abs(y)} steps {direction_y(y)} and {abs(x)} steps {direction_x(x)}"

    def reset_position(self):
        self.__position_xy = (0, 0)

    def __move_xy(self, steps_x, steps_y):
        x, y = self.__position_xy
        self.__position_xy = (x + steps_x, y + steps_y)

    def move_north(self):
        self.__move_xy(0, 1)

    def move_south(self):
        self.__move_xy(0, -1)

    def move_east(self):
        self.__move_xy(1, 0)

    def move_west(self):
        self.__move_xy(-1, 0)

    def is_alive(self):
        return self.lives > 0

    def notify_if_dead(self):
        if not self.is_alive():
            return f"{self.name} lost!"

    def attack_enemy(self, enemy):
        assert isinstance(enemy, Enemy)
        return enemy.receive_damage(self.attack)

    def receive_damage(self, damage):
        self.lives -= damage
        return self.notify_if_dead()


def direction_y(y):
    return "north" if y > 0 else "south"


def direction_x(x):
    return "east" if x > 0 else "west"
