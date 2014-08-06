def attack_function(caster, target=None):
    damage = caster.strength
    if target is not None:
        target.take_damage(damage)
    else:
        return damage

# all skills are wrapped this way
attack = ["Attack", attack_function]