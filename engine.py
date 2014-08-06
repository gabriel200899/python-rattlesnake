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