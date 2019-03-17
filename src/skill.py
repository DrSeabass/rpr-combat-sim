""" Represents a skill or spell"""
import math
import make_stats as stats


def base():
    return {
        'label' : "Stub",
        'level' : 0,
        'cost' : 0,
        'scales' : False, # what to do with half / powerful cast.
        'difficulty_mod' : 0
    }

def get_cost(skill, user):
    base = skill['cost']
    level_delta = user['level'] - skill['level']
    if level_delta < 0:
        return base * 2.5
    scale = min((1.0 * level_delta) / skill['level'], 1)
    return math.trunc(base * (1 - scale))

def scale_by_level(base, trgt_level):
    return {
        'label' : base['label'],
        'level' : trgt_level,
        'cost' : math.trunc((1.0 * base['cost'] * trgt_level) / stats.MAX_LEVEL),
        'scales' : base['scales'],
        'difficulty_mod' : base['difficulty_mod'],
        'damage' : 0
    }

def direct_damage_single_target_max():
    return {
        'label' : "Direct Damage, Single Target",
        'level' : stats.MAX_LEVEL,
        'cost' : stats.MAX_AP / 15,
        'scales' : True,
        'difficulty_mod' : 0,
        'damage' : stats.MAX_HP / 5
    }

def direct_damage_multi_target_max():
    return {
        'label' : "Direct Damage, Multi Target",
        'level' : stats.MAX_LEVEL,
        'cost' : stats.MAX_AP / 10,
        'scales' : True,
        'difficulty_mod' : 10,
        'damage' : stats.MAX_HP / 10
    }

def heal_single_target_max():
    return {
        'label' : "Heal, Single Target",
        'level' : stats.MAX_LEVEL,
        'cost' : stats.MAX_AP / 15,
        'scales' : True,
        'difficulty_mod' : 0,
        'damage' : -1 * (stats.MAX_HP / 5)
    }

def heal_multi_target_max():
    return {
        'label' : "Heal, Multi Target",
        'level' : stats.MAX_LEVEL,
        'cost' : stats.MAX_AP / 10,
        'scales' : True,
        'difficulty_mod' : 10,
        'damage' : -1 * (stats.MAX_HP / 10)
    }
