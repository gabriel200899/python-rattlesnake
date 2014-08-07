import help_strings


def fight(player, enemy):
    print("%s is fighting %s!" % (player.name, enemy.name))
    while player.life != 0:
        print(battle_status(player, enemy))
        while True:
            player_input = get_input()
            if player_input.isdigit() and 0 < eval(player_input) <= len(player.skills):
                player.skills[eval(player_input) - 1][1](player, enemy)
                break
            elif player_input == "":
                # if the player issued a command, get_input will return an empty string
                pass
            else:
                print("Invalid input. Try again.")
        # continue from here
        break


def get_input():
    # strip discards whitespaces
    player_input = ""
    while len(player_input) == 0:
        player_input = input(">>> ").strip().lower().split()
    if player_input[0] == 'quit' or player_input[0] == 'exit':
        game_exit()
    elif player_input[0] == 'help' or player_input[0] == '?':
        try:
            game_help(player_input[1])
        except IndexError:
            print("Syntax:\n\thelp [something]\n\t?    [something]")
    else:
        return player_input[0]
    return ""


def game_exit():
    exit(0)


def game_help(query):
    result = help_strings.help_strings.get(query)
    if result is not None:
        print(result)
    else:
        print("{} has no help text.".format(query))


def battle_status(player, enemy):
    output = ['%10s%-10s%15s%-10s' % ('', player.name, '', enemy.name),
              '%10s%-10s%5d%10s%-10s%5d' % ('', 'Level:', player.lvl, '', 'Level:', enemy.lvl),
              '%10s%-10s%5d%10s%-10s%5d' % ('', 'Life:', player.life, '', 'Life:', enemy.life),
              '%10s%-10s%5d%10s%-10s%5d' % ('', 'Mana:', player.mana, '', 'Mana:', enemy.mana),
              '    Skills:']
    # prints the player skills
    for i in range(len(player.skills)):
        output.append("%5d%20s (%d DMG)" % (i + 1, player.skills[i][0], player.skills[i][1](player)))
    # code here
    return '\n'.join(output)