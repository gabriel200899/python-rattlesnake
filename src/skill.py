def attack(caster, target):
    target.take_damage(caster.strength)

# all skills are wrapped this way
attack = ["Attack", attack]