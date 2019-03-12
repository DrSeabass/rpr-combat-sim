import math

MAX_STAT = 255

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

def god():
    stats = { 'label' : "",
              'strength' : MAX_STAT,
              'toughness': MAX_STAT,
              'dexterity': MAX_STAT,
              'speed' : MAX_STAT,
              'intellect' : MAX_STAT,
              'spirit' : MAX_STAT }
    compute_derived_stats(stats)
    return stats

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


def main():
    bs = god()
    print bs


if __name__ == '__main__':
    main()
