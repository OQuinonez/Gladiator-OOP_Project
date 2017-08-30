from random import randint


class Gladiator:
    def __init__(self, health, rage, damage_low, damage_high, name):
        """ (int, int, int, int, str, int) -> Gladiator
        Represents a Gladiator with the health, rage, the lowest
        damage possible, and the highest damage possible"""
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.name = name

    def __str__(self):
        """ (Gladiator) -> (Gladiator)
        Returns a string with the format
            health, rage, damage_low, damage_high
        >>> goku = Gladiator(100, 0, 5, 20)
        >>> print(goku)
        >>> Health: 100, Rage: 0, Damage_low: 5, Damage_high 20
        """
        return "{} || Health: {}, Rage: {}, Damage_low: {}, Damage_high: {}".format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def attack(self, other_g):
        """ Gladiator, Gladiator -> Gladiator, Gladiator
        """
        hit = randint(self.damage_low, self.damage_high)
        if randint(1, 100) <= self.rage:
            other_g.health = other_g.health - (hit * 2)
            self.rage = 0
        else:
            self.rage += 15
            other_g.health = other_g.health - hit

    def heal(self):
        ''' Gladiator -> Gladiator
        Function will heal the the gladiator by taking 10 rage
        to heal for 5 and the gladiator cannont heal over 100
        '''
        if self.rage >= 10:
            self.health = min(100, self.health + 5)
            self.rage = max(0, self.rage - 10)

    def is_dead(self):
        ''' Gladiator _> bool
        Function will return True iff has no health
        left
        '''
        if self.health <= 0:
            return True
        else:
            return False

    def rage_ing_up(self):
        ''' Gladiator -> Gladiator
        Function will add 20 to the rage if the gladiator
        chooses to pass
        '''
        if self.rage <= 100:
            self.rage = min(100, self.rage + 20)
            return Gladiator

    def __repr__(self):
        return 'Gladiator({}, {}, {}, {})'.format(
            repr(self.health),
            repr(self.rage), repr(self.damage_low), repr(self.damage_high))

    def haboken(self, opponent):
        ''' Gladiator, Gladiator -> 
        Function will take away hp from the defender from a range of 50 to 100
        '''
        fire = randint(40, 60)
        hit = randint(self.damage_low, self.damage_high)
        if self.rage >= 45:
            opponent.health = opponent.health - fire
            self.rage = 0
        else:
            self.rage += 15
            opponent.health = opponent.health - hit

    def dragon_kick(self, other_glad):
        ''' Gladiator, Gladiator ->
        New move an attacker can do against a defender
        The move can make any type of damage from the range of
        25 - 40 and requires atleast 40 rage
        '''
        hit = randint(self.damage_low, self.damage_high)
        kick = randint(25, 40)
        if self.rage >= 30:
            other_glad.health = other_glad.health - kick
            self.rage = 0
        else:
            other_glad.health = other_glad.health - hit
            self.rage += 15


class Gameplay:
    ''' class used to generate multiple characters for a game '''

    def __init__(self, gladiators):
        ''' [Gladiator] '''
        self.gladiators = gladiators

    def is_fighter(self, fighter_name):
        ''' returns true iff the fighter_name matches one of the fighters '''
        return fighter_name.lower() in [
            fighter.name.lower() for fighter in self.gladiators
        ]

    def get_fighter(self, fighter_name):
        for fighter in self.gladiators:
            if fighter.name.lower() == fighter_name.lower():
                return fighter