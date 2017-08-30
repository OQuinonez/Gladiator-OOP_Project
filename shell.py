import core
import time
from random import choice, randint
from termcolor import cprint


def beginning_skull():
    'Function will print a skull at the beginning of the gladiator game'
    cprint(
        "                                      ____                                              \n"
        "                                 __,---'     `--.__                                     \n"
        "                             ,-'                ; `.                                    \n"
        "                             ,'                  `--.`--.                               \n"
        "                             ,'                       `._ `-.                           \n"
        "                             ;                     ;     `-- ;                          \n"
        "                         ,-'-_       _,-~~-.      ,--      `.                           \n"
        "                         ;;   `-,;    ,'~`.__    ,;;;    ;  ;                           \n"
        "                         ;;    ;,'  ,;;      `,  ;;;     `. ;                           \n"
        "                         `:   ,'    `:;     __/  `.;      ; ;                           \n"
        "                             ;~~^.   `.   `---'~~    ;;      ; ;                        \n"
        "                             `,' `.   `.            .;;;     ;'                         \n"
        "                             ,',^. `.  `._    __    `:;     ,'                          \n"
        "                             `-' `--'    ~`--'~~`--.  ~    ,'                           \n"
        "                         /;`-;_ ; ;. /. /   ; ~~`-.     ;                               \n"
        "     -._                   ; ;  ; `,;`-;__;---;      `----'                             \n"
        "     `--.__             ``-`-;__;:  ;  ;__;                                             \n"
        "     ...     `--.__                `-- `-'                                              \n"
        "     `--.:::...     `--.__                ____                                          \n"
        "         `--:::::--.      `--.__    __,--'    `.                                        \n"
        "             `--:::`;....       `--'       ___  `.                                      \n"
        "                 `--`-:::...     __           )  ;                                      \n"
        "                     ~`-:::...   `---.      ( ,'                                        \n"
        "                         ~`-:::::::::`--.   `-.                                         \n"
        "                             ~`-::::::::`.    ;                                         \n"
        "                                 ~`--:::,'   ,'                                         \n"
        "                                     ~~`--'~                                            \n",
        'red',
        end="")


def mickey_mouse():
    ''' 
    Function will print a mickey mouse ascii whenever it is called
    '''
    cprint(
        '    ###########                                       \n'
        '  ###############        __-----__          ##        \n'
        '##################    ###          \       ####       \n'
        '################## #### #            \     # ##       \n'
        ' ####################            \~~\  \   ,##",      \n'
        '  #################       /~~\    \## \  \"     :     \n'
        '    ###############       \    \   \##" /       :     \n'
        '              #######       \### \    /         :     \n'
        '              #############  \###/             :      \n'
        '               ########                       :       \n'
        '                ######   __                  :        \n'
        '                 ####   /\                  /         \n'
        '      ############ ###    \\______________/|          \n'
        '    ##################     \ __         / /           \n'
        '  ####################\__    \  \---\,/ /             \n'
        '  ###################    \     \_____/ /              \n'
        '   #################       \_________/                \n'
        '    ###############                                   \n'
        '      ###########                                     \n',
        'red',
        end="")


def mega_man():
    '''
    prints the ascii every time megaman is choosen
    '''
    cprint(
        "         _..._                   \n"
        "      .'     '.                  \n"
        "     /`\     /`\    |\           \n"
        "    (__|     |__)|\  \\  /|      \n"
        "    (     '     ) \\ || //      \n"
        "     \         /   \\||//        \n"
        "      \   _   /  |\|`  /         \n"
        "       '.___.'   \____/          \n"
        "        (___)    (___)           \n"
        "      /`     `\  / /             \n"
        "     |         \/ /              \n"
        "     | |     |\  /               \n"
        "     | |     | '`                \n"
        "     | |     |                   \n"
        "     | |     |                   \n"
        "     |_|_____|                   \n"
        "    (___)_____)                  \n"
        "    /    \   |                   \n"
        "   /   |\|   |                   \n"
        "  //||\\  Y  |                   \n"
        " || || \\ |  |                   \n"
        " |/ \\ |\||  |                   \n"
        "     \||__|__|                   \n"
        "      (___|___)                  \n"
        "      /   A   \                  \n"
        "     /   / \   \                 \n"
        "    \___/   \___/                \n",
        'red',
        end="")


def make_players():
    gameplay = core.Gameplay([
        core.Gladiator(100, 0, randint(5, 9), randint(15, 25), 'Goku'),
        core.Gladiator(100, 0, randint(5, 9), randint(15, 25), 'Ryu'),
        core.Gladiator(100, 100, 50, 50, 'Mickey Mouse'),
        core.Gladiator(100, 0, randint(9, 14), randint(20, 30), 'Mega Man')
    ])
    return gameplay


def goku():
    ''' function will print goku every time it is called
    '''
    cprint(
        """                            _                                           \n"""
        """                    \'-._ _.--'~~'--._                                  \n"""
        """                        \   "            ^.    ___                      \n"""
        """                        /                  \.-~_.-~                     \n"""
        """                .-----'     /\/"\ /~-._      /                          \n"""
        """                /  __      _/\-.__\L_.-/\     "-.                       \n"""
        """            /.-"  \    ( ` \_o>"<o_/  \  .--._\                         \n"""
        """            /'      \    \:     "     :/_/     "`                       \n"""
        """                    /  /\ "\    ~    /~"                                \n"""
        """                    \ I  \/]"-._ _.-"[                                  \n"""
        """                ___ \|___/ ./    l   \___   ___                         \n"""
        """            .--v~   "v` ( `-.__   __.-' ) ~v"   ~v--.                   \n"""
        """        .-{   |     :   \_    "~"    _/   :     |   }-.                 \n"""
        """        /   \  |           ~-.,___,.-~           |  /   \               \n"""
        """        ]     \ |                                 | /     [             \n"""
        """        /\     \|     :                     :     |/     /\             \n"""
        """        /  ^._  _K.___,^                     ^.___,K_  _.^  \           \n"""
        """    /   /  "~/  "\                           /"  \~"  \   \             \n"""
        """    /   /    /     \ _          :          _ /     \    \   \           \n"""
        """    .^--./    /       Y___________l___________Y       \    \.--^.       \n"""
        """    [    \   /        |        [/    ]        |        \   /    ]       \n"""
        """    |     "v"         l________[____/]________j         }"     /        \n"""
        """    }------t          /                       \       /`-.     /        \n"""
        """    |      |         Y                         Y     /    "-._/         \n"""
        """    }-----v'         |         :               |     7-.     /          \n"""
        """    |   |_|          |         l               |    / . "-._/           \n"""
        """    l  .[_]          :          \              :  r[]/_.  /             \n"""
        """    \_____]                     "--.             "-.____/               \n""",
        'blue',
        end="")


def ryu():
    ''' function will print goku every time it is called
    '''
    cprint(
        """                            _                                           \n"""
        """                    \'-._ _.--'~~'--._                                  \n"""
        """                        \   "            ^.    ___                      \n"""
        """                        /                  \.-~_.-~                     \n"""
        """                .-----'     /\/"\ /~-._      /                          \n"""
        """                /  __      _/\-.__\L_.-/\     "-.                       \n"""
        """            /.-"  \    ( ` \_o>"<o_/  \  .--._\                         \n"""
        """            /'      \    \:     "     :/_/     "`                       \n"""
        """                    /  /\ "\    ~    /~"                                \n"""
        """                    \ I  \/]"-._ _.-"[                                  \n"""
        """                ___ \|___/ ./    l   \___   ___                         \n"""
        """            .--v~   "v` ( `-.__   __.-' ) ~v"   ~v--.                   \n"""
        """        .-{   |     :   \_    "~"    _/   :     |   }-.                 \n"""
        """        /   \  |           ~-.,___,.-~           |  /   \               \n"""
        """        ]     \ |                                 | /     [             \n"""
        """        /\     \|     :                     :     |/     /\             \n"""
        """        /  ^._  _K.___,^                     ^.___,K_  _.^  \           \n"""
        """    /   /  "~/  "\                           /"  \~"  \   \             \n"""
        """    /   /    /     \ _          :          _ /     \    \   \           \n"""
        """    .^--./    /       Y___________l___________Y       \    \.--^.       \n"""
        """    [    \   /        |        [/    ]        |        \   /    ]       \n"""
        """    |     "v"         l________[____/]________j         }"     /        \n"""
        """    }------t          /                       \       /`-.     /        \n"""
        """    |      |         Y                         Y     /    "-._/         \n"""
        """    }-----v'         |         :               |     7-.     /          \n"""
        """    |   |_|          |         l               |    / . "-._/           \n"""
        """    l  .[_]          :          \              :  r[]/_.  /             \n"""
        """    \_____]                     "--.             "-.____/               \n""",
        'yellow',
        end="")


def show_asii(player):
    ''' Helper funtion to make the rest of the shell look
    cleaner
    '''
    if player == 'mickey mouse':
        mickey_mouse()
    elif player == 'mega man':
        mega_man()
    elif player == 'goku':
        goku()
    elif player == 'ryu':
        ryu()


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
    gameplay = make_players()
    print_players()
    while True:
        player_one = input(
            'Player 1, who would you like to be? ').strip().lower()
        show_asii(player_one)
        player_two = input(
            'Player 2, who would you like to be? ').strip().lower()
        show_asii(player_two)
        if gameplay.is_fighter(player_one) and gameplay.is_fighter(player_two):
            first_player = gameplay.get_fighter(player_one)
            second_player = gameplay.get_fighter(player_two)
            break
        print("Invalid Choice")
    player_1, player_2 = first_player, second_player
    while True:
        battle(player_1, player_2)
        if player_2.is_dead():
            winner(player_1, player_2)
            exit()

        battle(player_2, player_1)
        if player_1.is_dead():
            winner(player_2, player_1)
            exit()


def one_player_game():
    gameplay = make_players()
    print_players()
    while True:
        character = input('Which one would you like to be? ').strip().lower()
        show_asii(character)
        individuals = ['goku', 'ryu', 'mega man', 'mickey mouse']
        rand_character = choice(individuals)
        print('You will be fighting against ', rand_character)
        show_asii(rand_character)
        if gameplay.is_fighter(character) and gameplay.is_fighter(
                rand_character):
            player_one = gameplay.get_fighter(character)
            player_two = gameplay.get_fighter(rand_character)
            break
        print('Invalid Choice')

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
    beginning_skull()
    while True:
        players = input("How many players? 1 or 2? ").strip()
        if players == '2':
            two_player_game()
        elif players == '1':
            one_player_game()


if __name__ == '__main__':
    main()