""" Representation of weapons"""
import math
import random
import matplotlib.pyplot as plot

## Damage Types
BLUNT = 0
SLASH = 1
PIERCE = 2

## Weapon Speed Range
MAX_WEAPON_SPEED=10
MED_WEAPON_SPEED=5
MIN_WEAPON_SPEED=1

## Weapon Damage Range
MAX_WEAPON_DAMAGE=500
MIN_WEAPON_DAMAGE=10

def fix_seed():
    random.seed(314159)

def base():
    return {
        'label' : 'stub',
        'speed' : 0,
        'min_dam' : 0,
        'max_dam' : 0,
        'dam_type' : BLUNT
}

def scale_weapon(weapon, level):
    """Scale supplied max-level weapon to given level"""
    ret_val = {}
    ret_val['label'] = weapon['label'] + " @ " + str(level)
    ret_val['speed'] = weapon['speed'] # weapon speeds don't scale!
    ret_val['min_dam'] = math.trunc(weapon['min_dam'] * (level / 100.))
    ret_val['max_dam'] = math.trunc(weapon['max_dam'] * (level / 100.))
    ret_val['dam_type'] = weapon['dam_type']
    return ret_val

######################## Weapon Definitions ###############################

## Fast and loose
def max_dagger():
    """high_speed_high_variance()"""
    return {
        'label' : 'Dagger',
        'speed' : MAX_WEAPON_SPEED,
        'dam_type' : PIERCE,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE / 5
    }

def max_basket_hilt():
    """high_speed_high_variance()"""
    return {
        'label' : 'Basket Hilt',
        'speed' : MAX_WEAPON_SPEED,
        'dam_type' : SLASH,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE / 5
    }

def max_sap():
    """high_speed_high_variance()"""
    return {
        'label' : 'Sap',
        'speed' : MAX_WEAPON_SPEED,
        'dam_type' : BLUDGEON,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE / 5
    }


## Fast and Tight
def max_epee():
    """high_speed_low_variance()"""
    return {
        'label' : 'Epee',
        'speed' : MAX_WEAPON_SPEED,
        'dam_type' : PIERCE,
        'min_dam' : MAX_WEAPON_DAMAGE / 10,
        'max_dam' : MAX_WEAPON_DAMAGE / 9
    }

def max_saber():
    """high_speed_low_variance()"""
    return {
        'label' : 'Saber',
        'speed' : MAX_WEAPON_SPEED,
        'dam_type' : SLASH,
        'min_dam' : MAX_WEAPON_DAMAGE / 10,
        'max_dam' : MAX_WEAPON_DAMAGE / 9
    }

def max_club():
    """high_speed_low_variance()"""
    return {
        'label' : 'Club',
        'speed' : MAX_WEAPON_SPEED,
        'dam_type' : BLUDGEON,
        'min_dam' : MAX_WEAPON_DAMAGE / 10,
        'max_dam' : MAX_WEAPON_DAMAGE / 9
    }

## Mid and loose

def max_estoc():
    """med_speed_max_variance()"""
    return {
        'label' : 'Estoc',
        'speed' : MED_WEAPON_SPEED,
        'dam_type' : PIERCE,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE / 3
    }

def max_longsword():
    """med_speed_max_variance()"""
    return {
        'label' : 'Longsword',
        'speed' : MED_WEAPON_SPEED,
        'dam_type' : SLASH,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE / 3
    }

def max_morningstar():
    """med_speed_max_variance()"""
    return {
        'label' : 'MorningStar',
        'speed' : MED_WEAPON_SPEED,
        'dam_type' : BLUDGEON,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE / 3
    }

## Mid and Tight

def max_bollock():
    """med_speed_min_variance()"""
    return {
        'label' : 'Bollock',
        'speed' : MED_WEAPON_SPEED,
        'dam_type' : PIERCE,
        'min_dam' : MAX_WEAPON_DAMAGE / 5,
        'max_dam' : MAX_WEAPON_DAMAGE / 4
    }

def max_broadsword():
    """med_speed_min_variance()"""
    return {
        'label' : 'Broadsword',
        'speed' : MED_WEAPON_SPEED,
        'dam_type' : SLASH,
        'min_dam' : MAX_WEAPON_DAMAGE / 5,
        'max_dam' : MAX_WEAPON_DAMAGE / 4
    }

def max_mace():
    """med_speed_max_variance()"""
    return {
        'label' : 'Mace',
        'speed' : MED_WEAPON_SPEED,
        'dam_type' : BLUDGEON,
        'min_dam' : MAX_WEAPON_DAMAGE / 5,
        'max_dam' : MAX_WEAPON_DAMAGE / 4
    }

## Slow and loose
def max_kryss():
    """min_speed_max_variance()"""
    return {
        'label' : 'Kryss',
        'speed' : MIN_WEAPON_SPEED,
        'dam_type' : PIERCE,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE
    }

def max_bastard():
    """min_speed_max_variance()"""
    return {
        'label' : 'BastardSword',
        'speed' : MIN_WEAPON_SPEED,
        'dam_type' : SLASH,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE
    }

def max_warhammer():
    """min_speed_max_variance()"""
    return {
        'label' : 'WarHammer',
        'speed' : MIN_WEAPON_SPEED,
        'dam_type' : BLUDGEON,
        'min_dam' : MIN_WEAPON_DAMAGE,
        'max_dam' : MAX_WEAPON_DAMAGE
    }


## Slow and Tight
def max_spear():
    """min_speed_min_variance()"""
    return {
        'label' : 'Spear',
        'speed' : MIN_WEAPON_SPEED,
        'dam_type' : PIERCE,
        'min_dam' : MAX_WEAPON_DAMAGE / 3,
        'max_dam' : MAX_WEAPON_DAMAGE / 2
    }

def max_glaive():
    """min_speed_min_variance()"""
    return {
        'label' : 'Glaive',
        'speed' : MIN_WEAPON_SPEED,
        'dam_type' : SLASH,
        'min_dam' : MAX_WEAPON_DAMAGE / 3,
        'max_dam' : MAX_WEAPON_DAMAGE / 2
    }

def max_quarterstaff():
    """min_speed_max_variance()"""
    return {
        'label' : 'QuarterStaff',
        'speed' : MIN_WEAPON_SPEED,
        'dam_type' : BLUDGEON,
        'min_dam' : MAX_WEAPON_DAMAGE / 3,
        'max_dam' : MAX_WEAPON_DAMAGE / 2
    }

######### Weapon Groupings
tight_variance_slash = [max_glaive(), max_broadsword(), max_saber()]
wide_variance_slash = [ max_bastard(), max_longsword(), max_basket_hilt() ]

heavy_hits_slash = [ max_bastard(), max_glaive()]
medium_hits_slash = [ max_broadsword(), max_longsword()]
light_hits_slash = [ max_saber(), max_basket_hilt() ]

########## Testing

def get_swings(weapon, weapon_levels=None, samples=100):
    damages = []
    averages = []
    mins = []
    maxs = []
    levels = None
    if weapon_levels is None:
        levels = range(1,100)
    else:
        levels = weapon_levels
    for level in levels:
        weapon_at_level = scale_weapon(weapon, level)
        mins.append(weapon_at_level['min_dam'])
        maxs.append(weapon_at_level['max_dam'])
        this_level = []
        sum = 0
        for sample in range(0, samples):
            this_dam = random.randint(weapon_at_level['min_dam'], weapon_at_level['max_dam'])
            sum += this_dam
            this_level.append(this_dam)
        averages.append((1.0 * sum) / samples)
        damages.append(this_level)
    return { 'damages' : damages,
             'average' : averages,
             'largest' : maxs,
             'smallest' : mins
             }
    

def plot_swings(weapon_list, weapon_levels=None, samples=100):
    for weapon in weapon_list:
        raw = get_swings(weapon, weapon_levels=weapon_levels, samples=samples)
        plot.plot(raw['average'], label=weapon['label'] + " Avg")
        plot.plot(raw['largest'], label=weapon['label'] + " Max")
        plot.plot(raw['smallest'], label=weapon['label'] + " Min")
    plot.xlabel("Level")
    plot.ylabel("Damage")
    plot.legend()
    plot.title(weapon['label'] + " damage by level")
    plot.grid(True)
    plot.show()

    
def main():
    plot_swings(wide_variance_slash, samples=100)

if __name__ == '__main__':
    main()
