import matplotlib.pyplot as plotter

import make_stats as stats
import enemy_stats as mobs

def points_derived_by_level(end_stats, derived):
    points = []
    for i in range(1, 101):
        points.append(mobs.stats_of_level(end_stats, i)[derived])
    return points

def plot_derived(stat_list, derived):
    stat_collection = []
    for stat in stat_list:
        plotter.plot(points_derived_by_level(stat, derived), label=stat['label'])
    plotter.xlabel('Level')
    plotter.ylabel(derived)
    plotter.title(derived + " by Level")
    plotter.legend()
    plotter.show()

def weak_phys ():
    god = mobs.god()
    minor_phys = mobs.minor_diety(stats.PHYSICAL)
    demi_split_phys = mobs.demigod(stats.MENTAL, stats.PHYSICAL)
    hero_weak_phys = mobs.hero(stats.PHYSICAL, stats.FINESSE)
    tough_weak_phys = mobs.tough(stats.PHYSICAL, stats.FINESSE)
    normal_weak_phys = mobs.normal(stats.PHYSICAL, stats.FINESSE)
    weenie_weak_phys = mobs.weenie(stats.PHYSICAL, stats.FINESSE)
    return [god, minor_phys, demi_split_phys, hero_weak_phys,
            tough_weak_phys, normal_weak_phys, weenie_weak_phys]

def weak_mental ():
    god = mobs.god()
    minor_ment = mobs.minor_diety(stats.MENTAL)
    demi_split_ment = mobs.demigod(stats.FINESSE, stats.MENTAL)
    hero_weak_ment = mobs.hero(stats.MENTAL, stats.FINESSE)
    tough_weak_ment = mobs.tough(stats.MENTAL, stats.FINESSE)
    normal_weak_ment = mobs.normal(stats.MENTAL, stats.FINESSE)
    weenie_weak_ment = mobs.weenie(stats.MENTAL, stats.FINESSE)
    return [god, minor_ment, demi_split_ment, hero_weak_ment,
            tough_weak_ment, normal_weak_ment, weenie_weak_ment]

def weak_finesse ():
    god = mobs.god()
    minor_finesse = mobs.minor_diety(stats.FINESSE)
    demi_split_finesse = mobs.demigod(stats.MENTAL, stats.FINESSE)
    hero_weak_finesse = mobs.hero(stats.FINESSE, stats.MENTAL)
    tough_weak_finesse = mobs.tough(stats.FINESSE, stats.MENTAL)
    normal_weak_finesse = mobs.normal(stats.FINESSE, stats.MENTAL)
    weenie_weak_finesse = mobs.weenie(stats.FINESSE, stats.MENTAL)
    return [god, minor_finesse, demi_split_finesse, hero_weak_finesse,
            tough_weak_finesse, normal_weak_finesse, weenie_weak_finesse]


if __name__ == '__main__':
    plot_derived(weak_phys(), 'max_hp')
    plot_derived(weak_mental(), 'max_ap')
    plot_derived(weak_finesse(), 'evasion')
    plot_derived(weak_phys(), 'physical_resist')
    plot_derived(weak_mental(), 'magic_attunement')
