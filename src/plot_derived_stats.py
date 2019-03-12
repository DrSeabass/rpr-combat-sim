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
    plotter.show()

if __name__ == '__main__':
    individual = stats.god()
    plot_derived([individual], 'max_hp')


