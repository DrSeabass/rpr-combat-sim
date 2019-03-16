import math

MAX_STAT = 255
PHYSICAL = 0
FINESSE = 1
MENTAL = 2

def base_stats():
    return {
        'label' : "",
        'level' : 100,
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
    base = min_val + 15 * base['level'] + 2 * str + tgh * 5
    rem = max_val - base
    half_rem = rem / 2
    tgh_str_boost = (tgh * str * 1.0) / (MAX_STAT * MAX_STAT)
    tgh_boost = (1.0 * tgh * tgh * tgh) / (MAX_STAT * MAX_STAT * MAX_STAT)
    return base + math.trunc(half_rem * tgh_str_boost + half_rem * tgh_boost)

def compute_max_ap(base):
    spr = base['spirit']
    inte = base['intellect']
    lvl = base['level']
    min_val = 10
    max_val = 1000
    baseVal = min_val + 3 * (lvl / 2) + (spr + inte) / 2
    rem = max_val - baseVal
    scale = 1 - 0.2 * (spr * inte) / (MAX_STAT * MAX_STAT) 
    boost = rem * (1.0 - scale ** (lvl/5))
    return baseVal + math.trunc(boost )

def compute_evasion(base):
    return (base['speed'] + base['dexterity'] / 2)

def compute_physical_resist(base):
    return (base['toughness'] + base['spirit'] / 2)

def compute_magic_attunement(base):
    return (base['intellect'] + base['dexterity'] / 2)

def compute_derived_stats(base):
    base['max_hp'] = compute_max_hp(base)
    base['max_ap'] = compute_max_ap(base)
    base['evasion'] = compute_evasion(base)
    base['physical_resist'] = compute_physical_resist(base)
    base['magic_attunement'] = compute_magic_attunement(base)

def stats_of_level(stats, level):
    ret_val = {
        'label' : stats['label'],
        'level' : level,
        'strength' : (stats['strength'] * level) / 100,
        'toughness' : (stats['toughness'] * level) / 100,
        'dexterity' : (stats['dexterity'] * level) / 100,
        'speed' : (stats['speed'] * level) / 100,
        'intellect' : (stats['intellect'] * level) / 100,
        'spirit' : (stats['spirit'] * level) / 100
    }
    compute_derived_stats(ret_val)
    return ret_val
    
