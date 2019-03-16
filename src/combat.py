""" Try to simulate combat for rpr"""
import random
import matplotlib.pyplot as plot
import make_stats as stats
import enemy_stats as mobs

MISS = 0   # whiff, no damage
GLANCE = 1 # glancing blow, half or quarter damage
HIT = 2    # solid hit, full damage
CRIT = 3   # beyond decent hit, 1.5x damage?

def fix_seed():
    random.seed(314159)

def check_hit(attacker, target):
    evade = target['evasion']
    acc = attacker['dexterity']
    evade_glance_thresh = 10
    possible_crit_thresh = 50
    attack_score = random.randint(0, acc)
    evade_score = random.randint(0, evade)
    crit_score = random.randint(0,4)
    contested_to_hit = attack_score - evade_score
    if contested_to_hit < 0:
        return MISS
    elif contested_to_hit < evade_glance_thresh:
        return GLANCE
    elif contested_to_hit < possible_crit_thresh:
        return HIT
    else:
        level_gap = attacker['level'] - target['level']
        if level_gap > 5:
            return CRIT
        elif crit_score > 0:
            return CRIT
        else:
            return HIT

def simulate_attacks(attack, target, samples=100):
    results = []
    for level in range(1,100):
        this_level = []
        atk_level = stats.stats_of_level(attack, level)
        trg_level = stats.stats_of_level(target, level)
        crit_count = 0
        hit_count = 0
        glance_count = 0
        miss_count = 0
        for s in range (0, samples):
            val = check_hit(atk_level, trg_level)
            if val == MISS:
                miss_count += 1
            elif val == GLANCE:
                glance_count += 1
            elif val == HIT:
                hit_count += 1
            elif val == CRIT:
                crit_count += 1
            this_level.append(val)
        print level, "\tmiss\t", miss_count, "\tglance\t", glance_count, "\thit\t", hit_count, "\tcrit\t", crit_count
        results.append(this_level)
    return results

def plot_attacks(attack, target, samples=100):
    data = simulate_attacks(attack, target, samples=samples)
    n, bins, patches = plot.hist(results, bins = CRIT + 1)
    plot.xlabel("Hit Type")
    plot.ylabel("Frequency")
    plot.title("To hit " + attack['label'] + " -> " + target['label'] + " by level")
    plot.grid(True)
    plot.show()
        
        
def main():
    hero_phys = mobs.hero(stats.MENTAL, stats.FINESSE)
    normal_phys = mobs.normal(stats.MENTAL, stats.FINESSE)
    simulate_attacks(hero_phys, normal_phys, samples=1000)

if __name__ == '__main__':
    main()
