
def base_stats():
    return {
        'strength' : 0,
        'toughness': 0,
        'dexterity': 0,
        'speed' : 0,
        'intellect' : 0,
        'spirit' : 0,
    }

def compute_max_hp(base):
    return base['strength'] + base['toughness'] + 10

def compute_max_ap(base):
    return base['spirit'] + base['intellect'] + 10

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


def main():
    bs = base_stats()
    compute_derived_stats(bs)
    print bs


if __name__ == '__main__':
    main()
