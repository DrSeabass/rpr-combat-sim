""" Try to simulate combat for rpr"""
import random
import matplotlib.pyplot as plot
import make_stats as stats
import enemy_stats as mobs
import skill

## Attack attempt outcome
MISS = 0   # whiff, no damage
GLANCE = 1 # glancing blow, half or quarter damage
HIT = 2    # solid hit, full damage
CRIT = 3   # beyond decent hit, 1.5x damage?

## Magic Attempt outcome
FIZZLE = 0       # no effect, 1/2 AP consumed
HALF_EFFECT = 1  # half effect, AP Consumed
FULL_CAST = 2    # Full effect, AP Consumed
POWER_CAST = 3   # Double Effect, AP Consumed
UNCONTROLLED = 4 # Quadruple Effect, Targets Multiple at Random, 2x AP consumed

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

def use_skill_spell(caster, spell):
    # note that spell casting isn't contested by the target, but by the spell!
    inte = caster['intellect']
    spr = caster['spirit']
    spell_level = spell['level']
    effective_level = spell_level + spell['difficulty_mod']
    scales = spell['scales']
    cost = skill.get_cost(spell, caster)
    level_delta = caster['level'] - effective_level
    level_rand = max(0, random.randint(1, caster['level']) + level_delta)
    mind_scale = 1 + ((inte * spr) * 1.0) / (stats.MAX_STAT * stats.MAX_STAT)
    fizz_thresh = 0.05 * effective_level
    half_thresh = 0.25 * effective_level
    normal_thresh = 0.5 * effective_level
    power_thresh = 0.8 *  effective_level
    uncontrolled_thresh = 0.98 * spell['level']
    cost_fraction =  (1.0 * cost) / caster['max_ap']
    #print effective_level, level_rand, normal_thresh
    if (level_rand * mind_scale) > uncontrolled_thresh:
        if random.random() < cost_fraction:
            return UNCONTROLLED
        else:
            if scales:
                return POWER_CAST
            else:
                return FULL_CAST
    elif (level_rand * mind_scale) > power_thresh:
        if scales:
            return POWER_CAST
        else:
            return FULL_CAST
    elif (level_rand * mind_scale) > normal_thresh:
        return FULL_CAST
    elif (level_rand * mind_scale) >  half_thresh:
        if scales:
            return HALF_EFFECT
        else:
            return FIZZLE
    else:
        return FIZZLE


def simulate_cast(caster, spell, cst_levels=None, spell_levels=None, samples=100):
    results = []
    for level in range(1,100):
        this_level = []
        cst_level = None
        spell_level = None
        if cst_levels is None:
            cst_level = stats.stats_of_level(caster, level)
        else:
            cst_level = stats.scale_by_level(caster, cst_levels[level])
        if spell_levels is None:
            spell_level = skill.scale_by_level(spell, level)
        else:
            spell_level = skill.scale_by_level(spell, spell_levels[level])
        fizz_count = 0
        hlf_count = 0
        full_count = 0
        power_count = 0
        uncnt_count = 0
        for s in range (0, samples):
            val = use_skill_spell(cst_level, spell_level)
            if val == FIZZLE:
                fizz_count += 1
            elif val == HALF_EFFECT:
                hlf_count += 1
            elif val == FULL_CAST:
                full_count += 1
            elif val == POWER_CAST:
                power_count += 1
            elif val == UNCONTROLLED:
                uncnt_count += 1
            this_level.append(val)
        print level, "\tfizzle\t", fizz_count, "\thalf\t", hlf_count, "\tfull\t", full_count, "\tpower\t", power_count, "\tuncontrolled\t", uncnt_count
        results.append(this_level)
    return results
            
def simulate_attacks(attack, target, atk_levels=None, trg_levels=None, samples=100):
    results = []
    for level in range(1,100):
        this_level = []
        atk_level = None
        trg_level = None
        if atk_levels is None:
            atk_level = stats.stats_of_level(attack, level)
        else:
            atk_level = stats.stats_of_level(attack, atk_levels[level])
        if trg_levels is None:
            trg_level = stats.stats_of_level(target, level)
        else:
            trg_level = stats.stats_of_level(target, trg_levels[level])
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
        
def main():
    hero_phys = mobs.hero(stats.MENTAL, stats.FINESSE)
    hero_fin = mobs.hero(stats.MENTAL, stats.PHYSICAL)
    hero_mnt = mobs.hero(stats.PHYSICAL, stats.FINESSE)
    normal_phys = mobs.normal(stats.MENTAL, stats.FINESSE)
    single_target_max = skill.direct_damage_single_target_max()
    #low_level_run = range(1,20) + ([20] * 81)
    #plot_attacks(hero_fin, normal_phys, atk_levels=low_level_run, samples=1000)
    #plot_attacks(hero_fin, normal_phys, samples=1000)
    #spell_10 = [10] * 100
    plot_casts(hero_mnt, single_target_max)#,spell_levels = spell_10)
    
    
if __name__ == '__main__':
    main()
