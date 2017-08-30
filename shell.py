import core
import time
from random import choice, randint

# , 'Goku'),core.Gladiator(100, 0, randint(5, 9), randint(15, 25), 'Ryu')])
# >>> l = 'a b c d e f g'.split()
# >>> l
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> ul = [ch.upper() for ch in l]
# >>> ul
# ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# >>> list(map(lambda s: s.upper(), l))
# ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# >>> gameplay.is_fighter('Goku')
# True
# >>> gameplay.is_fighter('Mickey Mouse')
# False
# >>> gameplay.gladiators.append(core.Gladiator(100, 100, 50, 50, 'Mickey Mouse'))
# >>> gameplay.is_fighter('Mickey Mouse')
# True
# >>> warrior = gameplay.get_fighter('Mickey Mouse')
# >>> warrior
# Gladiator(100, 100, 50, 50)
# >>> print(warrior)
# Mickey Mouse || Health: 100, Rage: 100, Damage_low: 50, Damage_high: 50
# >>> attacker = gameplay.get_fighter('Goku')
# >>> warrior.attack(attacker)
# >>> print(attacker)
# Goku || Health: 0, Rage: 0, Damage_low: 6, Damage_high: 21
# >>> attacker.is_dead()
# True


def make_players():
    gameplay = core.Gameplay([
        core.Gladiator(100, 0, randint(5, 9), randint(15, 25), 'Goku'),
        core.Gladiator(100, 0, randint(5, 9), randint(15, 25), 'Ryu'),
        core.Gladiator(100, 100, 50, 50, 'Mickey Mouse'),
        core.Gladiator(45, 0, randint(9, 14), randint(20, 30), 'Mega Man')
    ])
    return gameplay


def print_players():
    print('Goku, Ryu, Mickey Mouse, Mega Man')


def show_options():
    """ -> str
    prints the options the players can have
    """
    opt = [
        "1.\tAttack: Will make random damage between damage_low and damage_high",
        "2.\tHeal: Will heal 5 for 10 rage",
        "3.\tSkip: Will skip turn but adds 20 rage",
        "4.\tHaduken: Requires 45 rage and takes up to 60 HP off opponent",
        "5.\tDragon Kick: Requires 30 rage and takes up from 25 to 40 HP",
    ]
    print('\n'.join(opt))


def one_player(cpu, player):
    print('\nAttacker: {}\n\nDefender: {}\n'.format(cpu, player))
    show_options()
    while True:
        time.sleep(.5)
        answer = choice('1, 2, 3, 4, 5')
        if answer in '1 2 3 4 5'.split():
            break
        # print('Invalid choice')

    if answer == '1':
        cpu.attack(player)
        print(cpu.name, "Just attacked you!")
        time.sleep(.5)
    elif answer == '2':
        if cpu.health == 100:
            cpu.attack(player)
            print(cpu.name, "Chose to heal")
            time.sleep(.5)
        else:
            cpu.heal()
            time.sleep(.5)
            print(cpu.name, "Just attacked you!")
    elif answer == '3':
        cpu.rage_ing_up()
        print('Turn skipped, rage increased')
        time.sleep(.5)
    elif answer == '4':
        cpu.haboken(player)
        time.sleep(.5)
    elif answer == '5':
        cpu.dragon_kick(player)
        print(cpu.name, "Did the famous Haduken")
        print('')
        time.sleep(.5)
    elif answer == 'q':
        exit()


def battle(attacker, defender):
    print('\nAttacker: {}\n\nDefender: {}\n'.format(attacker, defender))
    show_options()
    while True:
        time.sleep(2)
        answer = input("\n{}, what would you like to do? ".format(
            attacker.name)).strip().lower()
        if answer in '1 2 3 4 5 q'.split():
            break
        print('Invalid choice')

    if answer == '1':
        attacker.attack(defender)
        time.sleep(.5)
    elif answer == '2':
        attacker.heal()
        time.sleep(.5)
    elif answer == '3':
        attacker.rage_ing_up()
        time.sleep(.5)
    elif answer == '4':
        attacker.haboken(defender)
        time.sleep(.5)
    elif answer == '5':
        attacker.dragon_kick(defender)
        time.sleep(.5)
    elif answer == 'q':
        exit()


def winner(winner, loser):
    print('\n\n', winner.name, 'Wins!')
    print(loser.name, 'Defeated...')


def two_player_game():
    dmg_low = randint(5, 9)
    dmg_high = randint(15, 25)
    goku = core.Gladiator(100, 0, 5, 20, 'Goku')
    rando = core.Gladiator(100, 0, 9, 16, 'Rando')
    print(goku, rando, sep="\n")
    while True:
        battle(goku, rando)
        if rando.is_dead():
            winner(goku, rando)
            exit()

        battle(rando, goku)
        if goku.is_dead():
            winner(rando, goku)
            exit()


def one_player_game():
    gameplay = make_players()
    print_players()
    # print(goku, ryu, sep="\n")
    while True:
        character = input('Which one would you like to be? ').strip().lower()
        individuals = ['goku', 'ryu', 'mega man', 'mickey mouse']
        rand_character = choice(individuals)
        if gameplay.is_fighter(character) and gameplay.is_fighter(
                rand_character):
            player_one = gameplay.get_fighter(character)
            player_two = gameplay.get_fighter(rand_character)
            break
        print('invalid choice')

    player_1, player_2 = player_one, player_two
    while True:
        battle(player_one, player_two)
        if player_two.is_dead():
            winner(player_one, player_two)
            exit()
        one_player(player_two, player_one)
        if player_one.is_dead():
            winner(player_two, player_one)
            exit()


def main():
    players = input("How many players? 1 or 2? ").strip()
    if players == '2':
        two_player_game()
    else:
        one_player_game()


if __name__ == '__main__':
    main()