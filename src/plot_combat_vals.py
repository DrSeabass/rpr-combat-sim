from combat import *

def plot_attacks(attack, target, atk_levels=None, trg_levels=None, samples=100):
    data = simulate_attacks(attack, target, atk_levels=atk_levels, trg_levels=trg_levels,
                            samples=samples)
    fix_seed()
    n, bins, patches = plot.hist(data, bins = CRIT + 1)
    plot.xlabel("Hit Type")
    plot.ylabel("Frequency")
    plot.title("To hit " + attack['label'] + " -> " + target['label'] + " by level")
    plot.grid(True)
    plot.show()

def plot_casts(caster, spell, cst_levels=None, spell_levels=None, samples=100):
    data = simulate_cast(caster, spell, cst_levels=cst_levels,
                         spell_levels=spell_levels, samples=samples)
    fix_seed()
    n, bins, patches = plot.hist(data, bins = UNCONTROLLED + 1)
    plot.xlabel("Cast Type")
    plot.ylabel("Frequency")
    plot.title(caster['label'] + " casts " + spell['label'] + " by level")
    plot.grid(True)
    plot.show()

    
def get_action_scores(character, levels = None, samples = 100):
    ret_val = []
    if levels is None:
        levels = range(1,100)
    for level in levels:
        this_level = []
        character_at_level = enemy_stats.stats_of_level(character, level)
        for i in range(0,samples):
            this_level.append(get_combat_action_score(character_at_level))
        ret_val.append(this_level)
    return ret_val

def plot_action_scores(characters, levels = None, samples = 5000):
    fix_seed()
    for character in characters:
        data = get_action_scores(character, levels = levels, samples = samples)
        for dataset in data:
            n, bins, patches = plot.hist(dataset)
    plot.xlabel("Combat Score")
    plot.ylabel("Frequency")
    plot.title("combat scores")
    plot.grid(True)
    plot.show()
    
        
def main():
    hero_phys = mobs.hero(stats.MENTAL, stats.FINESSE)
    hero_fin = mobs.hero(stats.MENTAL, stats.PHYSICAL)
    hero_mnt = mobs.hero(stats.FINESSE, stats.PHYSICAL)
    normal_phys = mobs.normal(stats.MENTAL, stats.FINESSE)
    single_target_max = skill.direct_damage_single_target_max()
    #low_level_run = range(1,20) + ([20] * 81)
    #plot_attacks(hero_fin, normal_phys, atk_levels=low_level_run, samples=1000)
    #plot_attacks(hero_fin, normal_phys, samples=1000)
    #spell_10 = [50] * 100
    #plot_casts(hero_mnt, single_target_max, spell_levels = spell_10)
    plot_action_scores([hero_phys, hero_fin, hero_mnt], levels = [10])
    
    
if __name__ == '__main__':
    main()

