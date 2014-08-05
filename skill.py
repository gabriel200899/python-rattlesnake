def attack_function(caster, target):
    target.take(caster.strength)

attack = {"Attack": attack_function}
