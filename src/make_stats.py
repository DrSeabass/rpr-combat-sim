import math

MAX_STAT = 255
PHYSICAL = 0
FINESSE = 1
MENTAL = 2

def base_stats():
    return {
        'label' : "",
        'strength' : 0,
        'toughness': 0,
        'dexterity': 0,
        'speed' : 0,
        'intellect' : 0,
        'spirit' : 0,
    }

def compute_max_hp(base):
    str = base['strength']
    tgh = base['toughness']
    min_val = 100
    max_val = 10000
    base = (min_val + str + 5 * tgh)
    rem = max_val - base
    boost = ((1.0 * str  * tgh) / (MAX_STAT * MAX_STAT))
    return base + math.trunc(rem * boost)

def compute_max_ap(base):
    return base['spirit'] + base['intellect'] + 90

def compute_evasion(base):
    return base['speed'] + base['dexterity']

def compute_physical_resist(base):
    return base['toughness'] + base['spirit']

def compute_magic_attunement(base):
    return base['intellect'] + base['dexterity']


def compute_derived_stats(base):
    base['max_hp'] = compute_max_hp(base)
    base['max_ap'] = compute_max_ap(base)
    base['evasion'] = compute_evasion(base)
    base['physical_resist'] = compute_physical_resist(base)
    base['magic_attunement'] = compute_magic_attunement(base)

def stats_of_level(stats, level):
    ret_val = {
        'strength' : (stats['strength'] * level) / 100,
        'toughness' : (stats['toughness'] * level) / 100,
        'dexterity' : (stats['dexterity'] * level) / 100,
        'speed' : (stats['speed'] * level) / 100,
        'intellect' : (stats['intellect'] * level) / 100,
        'spirit' : (stats['spirit'] * level) / 100
    }
    compute_derived_stats(ret_val)
    return ret_val
    
def god():
    stats = { 'label' : "God",
              'strength' : MAX_STAT,
              'toughness': MAX_STAT,
              'dexterity': MAX_STAT,
              'speed' : MAX_STAT,
              'intellect' : MAX_STAT,
              'spirit' : MAX_STAT }
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
        base['label'] = ", Halfed Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif half_two == FINESSE:
        base['label'] = ", Halfed Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif half_two == MENTAL:
        base['label'] = ", Halfed Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    compute_derived_stats(base)
    return base

def decent(half_one, half_two):
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
        base['label'] = ", Halfed Physical"
        base['strength'] = math.trunc(0.5 * base['strength'])
        base['toughness'] = math.trunc(0.5 * base['toughness'])
    elif half_two == FINESSE:
        base['label'] = ", Halfed Finesse"
        base['dexterity'] = math.trunc(0.5 * base['dexterity'])
        base['speed'] = math.trunc(0.5 * base['speed'])
    elif half_two == MENTAL:
        base['label'] = ", Halfed Mental"
        base['intellect'] = math.trunc(0.5 * base['intellect'])
        base['spirit'] = math.trunc(0.5 * base['spirit'])
    if ((half_one == PHYSICAL and half_two == FINESSE) or
        (half_two == PHYSICAL and half_one == FINESSE)):
        base['intellect'] = match.truc(0.75 * base['intellect'])
        base['spirit'] = match.truc(0.75 * base['spirit'])
    elif ((half_one == PHYSICAL and half_two == Mental) or
          (half_two == PHYSICAL and half_one == Mental)):
        base['dexterity'] = math.trunc(0.75 * base['dexterity'])
        base['speed'] = math.trunc(0.75 * base['speed'])
    elif ((half_one == FINESSE and half_two == MENTAL) or
          (half_two == FINESSE and half_two == MENTAL)):
        base['strength'] = math.trunc(0.75 * base['strength'])
        base['toughness'] = math.trunc(0.75 * base['toughness'])
    compute_derived_stats(base)
    return base

def normal():
    return None

def weenie():
    return None
        
def main():
    bs = god()
    print bs

if __name__ == '__main__':
    main()
