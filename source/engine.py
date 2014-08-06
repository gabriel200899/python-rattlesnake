def fight(player, enemy):
    print("%s is fighting %s!" % (player.name, enemy.name))
    while player.life != 0:
        print(battle_status(player, enemy))
        while True:
            # strip discards whitespaces
            player_input = input(">>> ").strip()
            if player_input.isdigit() and 0 < eval(player_input) <= len(player.skills):
                player.skills[eval(player_input) - 1][1](player, enemy)
                break
            else:
                print("Invalid input. Try again.")
        # continue from here
        break


def battle_status(player, enemy):
    output = ['%10s%-10s%14s%-10s' % ('', player.name, '', enemy.name),
              '%10s%-10s%4d%10s%-10s%4d' % ('', 'Level:', player.lvl, '', 'Level:', enemy.lvl), ' Skills:']
    # prints the player skills
    for i in range(len(player.skills)):
        output.append("%2d%10s" % (i + 1, player.skills[i][0]))
    # code here
    return '\n'.join(output)