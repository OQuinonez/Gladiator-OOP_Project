import core
from random import randint


class TestGladiator:
    def setup(self):
        self.glad = core.Gladiator(100, 0, 5, 20, 'Bob')

    def test_class_Gladiator_works(self):
        assert isinstance(core.Gladiator, type)

    def test_gladiator_str(self):
        assert str(
            self.glad
        ) == "Bob || Health: 100, Rage: 0, Damage_low: 5, Damage_high: 20"

    def test_Gladiator_repr(self):
        assert repr(self.glad) == 'Gladiator(100, 0, 5, 20)'

    def test_Gladiator_init_works(self):
        ''' test init to check for the following parameters
        health, rage, damage_low, damage_high, name
        '''
        g = core.Gladiator(100, 0, 5, 20, 'Bob')
        assert g.health == 100
        assert g.rage == 0
        assert g.damage_low == 5
        assert g.damage_high == 20
        assert g.name == 'Bob'

    def test_attack(self):
        player_1 = core.Gladiator(100, 0, 5, 20, 'a')
        player_2 = core.Gladiator(100, 0, 3, 23, 'b')
        player_1.attack(player_2)
        assert player_1.rage == 15
        assert player_2.health <= 95 and player_2.health >= 80

        player_1 = core.Gladiator(100, 100, 5, 20, 'a')
        player_2 = core.Gladiator(100, 0, 3, 23, 'b')
        rand = randint(1, 100)
        player_1.attack(player_2)
        assert player_1.rage == 0
        assert player_2.health >= 40 and player_2.health <= 90

    def test_heal(self):
        player_1 = core.Gladiator(35, 40, 5, 20, 'a')
        player_1.heal()
        assert player_1.rage == 30
        assert player_1.health == 40

    def test_is_dead(self):
        player_1 = core.Gladiator(0, 40, 5, 20, 'a')
        actual = player_1.is_dead()
        expect = True
        assert actual == expect

        player_1 = core.Gladiator(1, 40, 5, 20, 'a')
        actual = player_1.is_dead()
        expect = False
        assert actual == False

    def test_rage_ing_up(self):
        player_1 = core.Gladiator(90, 40, 5, 20, 'a')
        actual = player_1.rage_ing_up()
        assert player_1.rage == 60

    def test_haboken(self):
        player_1 = core.Gladiator(100, 45, 5, 20, 'a')
        player_2 = core.Gladiator(100, 0, 3, 23, 'b')
        player_1.haboken(player_2)
        assert player_1.rage == 0
        assert player_2.health <= 60 and player_2.health >= 40

        player_1 = core.Gladiator(100, 10, 5, 20, 'a')
        player_2 = core.Gladiator(100, 0, 3, 23, 'b')
        player_1.haboken(player_2)
        assert player_1.rage == 25
        assert player_2.health <= 95 and player_2.health >= 80