import combat
import enemy_stats as chars
import make_stats as stats
import enemy_groups as mobs

def main():
    hero_phys = chars.hero(stats.MENTAL, stats.FINESSE)
    hero_fin = chars.hero(stats.MENTAL, stats.PHYSICAL)
    hero_mnt = chars.hero(stats.FINESSE, stats.PHYSICAL)
    party = [hero_fin, hero_phys, hero_mnt]
    costs = combat.sample_combat(party, mobs.tough_decent, at_level = 75)
    print "Final Combat Expense", costs
    
    
if __name__ == '__main__':
    main()
