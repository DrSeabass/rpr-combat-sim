import matplotlib.pyplot as plotter

import make_stats as stats

def points_derived_by_level(end_stats, derived):
    points = []
    for i in range(1, 101):
        points.append(stats.stats_of_level(end_stats, i)[derived])
    return points

def plot_derived(stat_list, derived):
    stat_collection = []
    for stat in stat_list:
        plotter.plot(points_derived_by_level(stat, derived), label=stat['label'])
    plotter.xlabel('Level')
    plotter.ylabel(derived)
    plotter.title("HP by Level")
    plotter.legend()
    plotter.show()

if __name__ == '__main__':
    god = stats.god()
    minor = stats.minor_diety(stats.PHYSICAL)
    demi_split_phys = stats.demigod(stats.MENTAL, stats.PHYSICAL)
    hero_weak_phys = stats.hero(stats.PHYSICAL, stats.FINESSE)
    tough_weak_phys = stats.tough(stats.PHYSICAL, stats.FINESSE)
    normal_weak_phys = stats.normal(stats.PHYSICAL, stats.FINESSE)
    weenie_weak_phys = stats.weenie(stats.PHYSICAL, stats.FINESSE)
    plot_derived([god, minor, demi_split_phys, hero_weak_phys,
                  tough_weak_phys, normal_weak_phys, weenie_weak_phys], 'max_hp')
