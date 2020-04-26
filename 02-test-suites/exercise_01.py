import unittest
from game import Enemy
from game import Player


class EnemyInitTest(unittest.TestCase):
    def test_enemy_init(self):
        e = Enemy("orc")
        self.assertEqual(e.name, "orc")
        self.assertEqual(e.lives, 1)


class EnemyDamageTest(unittest.TestCase):
    def test_enemy_takes_damage(self):
        e = Enemy("goblin")
        e.receive_damage(1)
        self.assertEqual(e.lives, 0)


class PlayerMovement(unittest.TestCase):
    def setUp(self):
        self.player = Player("Link")

    def test_move_north(self):
        self.player.reset_position()
        self.player.move_north()
        self.assertEqual(self.player.position_xy, (0, 1))

    def test_move_east(self):
        self.player.reset_position()
        self.player.move_east()
        self.assertEqual(self.player.position_xy, (1, 0))

    def test_pretty_position(self):
        self.player.move_south()
        self.player.move_south()
        self.player.move_west()
        self.player.move_west()
        self.assertEqual(
            self.player.pretty_position(), "Link went 2 steps south and 2 steps west"
        )


class PlayerDamage(unittest.TestCase):
    def setUp(self):
        self.player = Player("Mario")
        self.enemy = Enemy("Bowser")

    def test_player_attack(self):
        result = self.player.attack_enemy(self.enemy)
        self.assertEqual(self.enemy.lives, 0)
        self.assertFalse(self.enemy.is_alive())
        self.assertEqual(result, "Bowser lost!")


enemySuite = unittest.TestSuite()
enemySuite.addTests(
    [
        EnemyInitTest("test_enemy_init"),
        EnemyDamageTest("test_enemy_takes_damage"),
        PlayerDamage("test_player_attack"),
    ]
)

playerSuite = unittest.TestSuite()
playerSuite.addTests(
    [
        PlayerMovement("test_move_north"),
        PlayerMovement("test_move_east"),
        PlayerMovement("test_pretty_position"),
        PlayerDamage("test_player_attack"),
    ]
)
