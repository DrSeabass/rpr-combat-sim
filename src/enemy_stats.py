from make_stats import *
import skill
import weapons

def god():
    stats = { 'label' : "God",
              'level' : 100,
              'strength' : MAX_STAT,
              'toughness': MAX_STAT,
              'dexterity': MAX_STAT,
              'speed' : MAX_STAT,
              'intellect' : MAX_STAT,
              'spirit' : MAX_STAT,
              'HEAL' : skill.heal_single_target_max(),
              'SKILL-ATTACK' : skill.direct_damage_single_target_max(),
              'PHYS-ATTACK' : weapons.max_bastard()
    }
    compute_derived_stats(stats)
    return stats

def minor_diety(weak_group):
    base = god()
    if weak_group == PHYSICAL:
        base['label'] = "Minor Diety - Weak Physical"
        base['strength'] = math.trunc(0.75 * base['strength'])
        base['toughness'] = math.trunc(0.75 * base['toughness'])
    elif weak_group == FINESSE:
        base['label'] = "Minor Diety - Weak Finesse"
        base['dexterity'] = math.trunc(0.75 * base['dexterity'])
        base['speed'] = math.trunc(0.75 * base['speed'])
    elif weak_group == MENTAL:
        base['label'] = "Minor Diety - Weak Mental"
        base['intellect'] = math.trunc(0.75 * base['intellect'])
        base['spirit'] = math.trunc(0.75 * base['spirit'])
    compute_derived_stats(base)
    return base

def demigod(weak_group, split_group):
    base = god()
    # weak group
    if weak_group == PHYSICAL:
        base['label'] = "Demigod - Weak Physical"
        base['strength'] = math.trunc(0.75 * base['strength'])
        base['toughness'] = math.trunc(0.75 * base['toughness'])
    elif weak_group == FINESSE:
        base['label'] = "Demigod - Weak Finesse"
        base['dexterity'] = math.trunc(0.75 * base['dexterity'])
        base['speed'] = math.trunc(0.75 * base['speed'])
    elif weak_group == MENTAL:
        base['label'] = "Demigod - Weak Mental"
        base['intellect'] = math.trunc(0.75 * base['intellect'])
        base['spirit'] = math.trunc(0.75 * base['spirit'])
    # split group
    if split_group == PHYSICAL:
        base['label'] += ", Split Physical"
        base['strength'] = math.trunc(0.875 * base['strength'])
        base['toughness'] = math.trunc(0.875 * base['toughness'])
    elif split_group == FINESSE:
        base['label'] += ", Split Finesse"
        base['dexterity'] = math.trunc(0.875 * base['dexterity'])
        base['speed'] = math.trunc(0.875 * base['speed'])
    elif split_group == MENTAL:
        base['label'] += ", Split Mental"
        base['intellect'] = math.trunc(0.875 * base['intellect'])
        base['spirit'] = math.trunc(0.875 * base['spirit'])
    compute_derived_stats(base)
    return base

def hero(weak_group, medium_group):
    base = god()
    # weak group
    if weak_group == PHYSICAL:
        base['label'] = "Hero - Weak Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif weak_group == FINESSE:
        base['label'] = "Hero - Weak Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif weak_group == MENTAL:
        base['label'] = "Hero - Weak Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    # medium group
    if medium_group == PHYSICAL:
        base['label'] += ", Medium Physical"
        base['strength'] = math.trunc(0.75 * base['strength'])
        base['toughness'] = math.trunc(0.75 * base['toughness'])
    elif medium_group == FINESSE:
        base['label'] += ", Medium Finesse"
        base['dexterity'] = math.trunc(0.75 * base['dexterity'])
        base['speed'] = math.trunc(0.75 * base['speed'])
    elif medium_group == MENTAL:
        base['label'] += ", Medium Mental"
        base['intellect'] = math.trunc(0.75 * base['intellect'])
        base['spirit'] = math.trunc(0.75 * base['spirit'])
    compute_derived_stats(base)
    return base

def tough(half_one, half_two):
    if (half_two > half_one):
        return tough(half_two, half_one)
    base = god()
    # weak group
    if half_one == PHYSICAL:
        base['label'] = "Tough - Halfed Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif half_one == FINESSE:
        base['label'] = "Tough - Halfed Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif half_one == MENTAL:
        base['label'] = "Tough - Halfed Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    if half_two == PHYSICAL:
        base['label'] += ", Halfed Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif half_two == FINESSE:
        base['label'] += ", Halfed Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif half_two == MENTAL:
        base['label'] += ", Halfed Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    compute_derived_stats(base)
    return base

def decent(half_one, half_two):
    if (half_two > half_one):
        return decent(half_two, half_one)
    base = god()
    # weak group
    if half_one == PHYSICAL:
        base['label'] = "Decent - Halfed Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif half_one == FINESSE:
        base['label'] = "Decent - Halfed Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif half_one == MENTAL:
        base['label'] = "Decent - Halfed Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    if half_two == PHYSICAL:
        base['label'] += ", Halfed Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif half_two == FINESSE:
        base['label'] += ", Halfed Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif half_two == MENTAL:
        base['label'] += ", Halfed Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    if ((half_one == PHYSICAL and half_two == FINESSE) or
        (half_two == PHYSICAL and half_one == FINESSE)):
        base['intellect'] = math.trunc(0.75 * base['intellect'])
        base['spirit'] = math.trunc(0.75 * base['spirit'])
    elif ((half_one == PHYSICAL and half_two == MENTAL) or
          (half_two == PHYSICAL and half_one == MENTAL)):
        base['dexterity'] = math.trunc(0.75 * base['dexterity'])
        base['speed'] = math.trunc(0.75 * base['speed'])
    elif ((half_one == FINESSE and half_two == MENTAL) or
          (half_two == FINESSE and half_two == MENTAL)):
        base['strength'] = math.trunc(0.75 * base['strength'])
        base['toughness'] = math.trunc(0.75 * base['toughness'])
    compute_derived_stats(base)
    return base

def normal(weak1, weak2):
    if weak2 > weak1:
        return normal(weak2, weak1)
    base = god()
    # weak group
    if weak1 == PHYSICAL:
        base['label'] = "Normal - Weak Physical"
        base['strength'] = math.trunc(0.2 * base['strength'])
        base['toughness'] = math.trunc(0.2 * base['toughness'])
    elif weak1 == FINESSE:
        base['label'] = "Normal - Weak Finesse"
        base['dexterity'] = math.trunc(0.2 * base['dexterity'])
        base['speed'] = math.trunc(0.2 * base['speed'])
    elif weak1 == MENTAL:
        base['label'] = "Normal - Weak Mental"
        base['intellect'] = math.trunc(0.2 * base['intellect'])
        base['spirit'] = math.trunc(0.2 * base['spirit'])
    if weak2 == PHYSICAL:
        base['label'] += ", Weak Physical"
        base['strength'] = math.trunc(0.2 * base['strength'])
        base['toughness'] = math.trunc(0.2 * base['toughness'])
    elif weak2 == FINESSE:
        base['label'] += ", Weak Finesse"
        base['dexterity'] = math.trunc(0.2 * base['dexterity'])
        base['speed'] = math.trunc(0.2 * base['speed'])
    elif weak2 == MENTAL:
        base['label'] += ", Weak Mental"
        base['intellect'] = math.trunc(0.2 * base['intellect'])
        base['spirit'] = math.trunc(0.2 * base['spirit'])
    if ((weak1 == PHYSICAL and weak2 == FINESSE) or
        (weak2 == PHYSICAL and weak1 == FINESSE)):
        base['intellect'] = math.trunc(0.4 * base['intellect'])
        base['spirit'] = math.trunc(0.4 * base['spirit'])
    elif ((weak1 == PHYSICAL and weak2 == MENTAL) or
          (weak2 == PHYSICAL and weak1 == MENTAL)):
        base['dexterity'] = math.trunc(0.4 * base['dexterity'])
        base['speed'] = math.trunc(0.4 * base['speed'])
    elif ((weak1 == FINESSE and weak2 == MENTAL) or
          (weak2 == FINESSE and weak2 == MENTAL)):
        base['strength'] = math.trunc(0.4 * base['strength'])
        base['toughness'] = math.trunc(0.4 * base['toughness'])
    compute_derived_stats(base)
    return base

def weenie(weak1, weak2):
    if weak2 > weak1:
        return weenie(weak2, weak1)
    if weak1 == weak2:
        #print "You can't double up on weenie weakness!"
        return None
    base = god()
    # weak group
    if weak1 == PHYSICAL:
        base['label'] = "Weenie - Weak Physical"
        base['strength'] = math.trunc(0.125 * base['strength'])
        base['toughness'] = math.trunc(0.125 * base['toughness'])
    elif weak1 == FINESSE:
        base['label'] = "Weenie - Weak Finesse"
        base['dexterity'] = math.trunc(0.125 * base['dexterity'])
        base['speed'] = math.trunc(0.125 * base['speed'])
    elif weak1 == MENTAL:
        base['label'] = "Weenie - Weak Mental"
        base['intellect'] = math.trunc(0.125 * base['intellect'])
        base['spirit'] = math.trunc(0.125 * base['spirit'])
    if weak2 == PHYSICAL:
        base['label'] += ", Weak Physical"
        base['strength'] = math.trunc(0.125 * base['strength'])
        base['toughness'] = math.trunc(0.125 * base['toughness'])
    elif weak2 == FINESSE:
        base['label'] += ", Weak Finesse"
        base['dexterity'] = math.trunc(0.125 * base['dexterity'])
        base['speed'] = math.trunc(0.125 * base['speed'])
    elif weak2 == MENTAL:
        base['label'] += ", Weak Mental"
        base['intellect'] = math.trunc(0.125 * base['intellect'])
        base['spirit'] = math.trunc(0.125 * base['spirit'])
    if ((weak1 == PHYSICAL and weak2 == FINESSE) or
        (weak2 == PHYSICAL and weak1 == FINESSE)):
        base['intellect'] = math.trunc(0.25 * base['intellect'])
        base['spirit'] = math.trunc(0.25 * base['spirit'])
    elif ((weak1 == PHYSICAL and weak2 == MENTAL) or
          (weak2 == PHYSICAL and weak1 == MENTAL)):
        base['dexterity'] = math.trunc(0.25 * base['dexterity'])
        base['speed'] = math.trunc(0.25 * base['speed'])
    elif ((weak1 == FINESSE and weak2 == MENTAL) or
          (weak2 == FINESSE and weak2 == MENTAL)):
        base['strength'] = math.trunc(0.25 * base['strength'])
        base['toughness'] = math.trunc(0.25 * base['toughness'])
    compute_derived_stats(base)
    return base

# You could move the min stats up, and not go level 15-100 Instead,
# you could set the minimum stat at 10, then things would scale about
# as well.

# That seems reasonable, but does not work.  Enemies scale the same way,
# so they just end up with a larger leg up on the PCs.  You have to start things
# around level 14 or so.
def stats_of_level(stats, level):
    ret_val = {
        'label' : stats['label'],
        'level' : level,
        'strength' : max(1, (stats['strength'] * level) / 100),
        'toughness' : max(1,(stats['toughness'] * level) / 100),
        'dexterity' : max(1,(stats['dexterity'] * level) / 100),
        'speed' : max(1, (stats['speed'] * level) / 100),
        'intellect' : max(1, (stats['intellect'] * level) / 100),
        'spirit' : max(1,(stats['spirit'] * level) / 100),
        'HEAL' : max(1,skill.scale_by_level(stats['HEAL'], level)),
        'SKILL-ATTACK' : skill.scale_by_level(stats['SKILL-ATTACK'], level),
        'PHYS-ATTACK' : weapons.scale_weapon(stats['PHYS-ATTACK'], level)
    }
    compute_derived_stats(ret_val)
    return ret_val

def party_of_level(party, level):
    ret_val = []
    for pmem in party:
        ret_val.append(stats_of_level(pmem, level))
    return ret_val

def main():
    w1 = weenie(PHYSICAL, FINESSE)
    w2 = weenie(PHYSICAL, MENTAL)
    w3 = weenie(FINESSE, MENTAL)
    print("Phys, Finnesse", w1)
    print("Phys, Mental", w2)
    print("Finesse, Mental", w3)

if __name__ == '__main__':
    main()
