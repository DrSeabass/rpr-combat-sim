""" Represents a skill or spell"""

def base():
    return {
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
    
    
