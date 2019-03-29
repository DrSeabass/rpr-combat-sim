import combat
import enemy_stats as chars
import make_stats as stats
import enemy_groups as mobs
import math
import matplotlib.pyplot as plt

def compute_mean_err(data):
    tot = 0
    els = 0
    for mem in data:
        tot += mem
        els += 1
    ssvar = 0
    arith_mean = (tot * 1.0) / els
    for mem in data:
        ssvar += (arith_mean - mem)**2
    ssvar *= (1.0 / els)
    ssvar = math.sqrt(ssvar)
    root_els = math.sqrt(els)
    return {
        'mean' : arith_mean,
        'std' : ssvar,
        '95_cid' : 1.96 * (ssvar / root_els)
    }
        

def sample_by_level(party,enemies):
    data = []
    for level in range(1,100):
        data.append(combat.sample_combat(party, enemies, at_level=level))
    return data

def win_loss_by_level(party, enemies_groups, group_names=None, data=None):
    if data is None:
        data = []
        for enemies in enemies_groups:
            data.append(sample_by_level(party,enemies))
    plt.xlabel("Level")
    plt.ylabel("P(Party Win)")
    index = -1
    for by_enemy_group in data:
        means = []
        err = []
        index += 1
        for by_level in by_enemy_group:
            these_values = []
            for record in by_level:
                if record['party_survives']:
                    these_values.append(1)
                else:
                    these_values.append(0)
            summary = compute_mean_err(these_values)
            means.append(summary['mean'])
            err.append(summary['95_cid'])
        if group_names is None:
            plt.errorbar(range(1,100), means, yerr=err)
        else:
            plt.errorbar(range(1,100), means, yerr=err, label=group_names[index])
    plt.legend()
    plt.show()
    

def main():
    hero_phys = chars.hero(stats.MENTAL, stats.FINESSE)
    hero_fin = chars.hero(stats.MENTAL, stats.PHYSICAL)
    hero_mnt = chars.hero(stats.FINESSE, stats.PHYSICAL)
    party = [hero_fin, hero_phys, hero_mnt]
    win_loss_by_level(party, [mobs.tough_decent, mobs.tough_weenie, mobs.decent_normal, mobs.normal_all, mobs.normal_weenie],
                      ['tough_decent', 'tough-weenie', 'decent-normal', 'normal_all', 'normal_weenie'])
    
    
if __name__ == '__main__':
    main()
