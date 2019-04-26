""" Try to simulate combat for rpr"""
import math
import random
import matplotlib.pyplot as plot
import make_stats as stats
import enemy_stats as chars
import enemy_groups as mobs
import skill

## PRINTF DEBUGGING
LOUD = False

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

## Other
DEFAULT_ACTION_COST = 10

def fix_seed():
    random.seed(314159)

ACTION_DIE_DIV = 20
ACTION_DIE = 3
    
def get_combat_action_score(character):
    base_val = character['level'] / 3.0  + 2.5 * character['speed']
    num_die = int(math.ceil(1 + base_val / ACTION_DIE_DIV))
    #print base_val, num_die
    sum = 0
    for i in range(0,num_die):
        sum += random.randint(1,ACTION_DIE)
    return sum
    
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

def do_atk_dam(attacker, target, weapon_min_dam, weapon_max_dam, hit_type):
    phys_resist = target['physical_resist']
    strength = attacker['strength']
    effective_resist = (1.0 *  phys_resist) / strength
    damage_boost = 1 + ((1.0 * strength) / stats.MAX_STAT)
    damage_roll = random.randint(weapon_min_dam, weapon_max_dam)
    damage = damage_boost * (damage_roll - effective_resist)
    return math.trunc(damage)

def do_spell_dam(caster, targets, spell, cast_type):
    caster_attune = caster['magic_attunement']
    caster_boost = 1 + (1.0 * caster_attune) / stats.MAX_STAT
    damages = []
    base_dam = spell['damage']
    if cast_type == FIZZLE:
        return [0]
    if cast_type == UNCONTROLLED:
        base_dam *= 4
        caster['current_hp'] - base_dam
    # setup damage base on caster type
    elif cast_type == HALF_EFFECT:
        base_dam *= 0.5
    elif cast_type == POWER_CAST:
        base_dam *= 2
    for target in targets:
        target_attune = target['magic_attunement']
        delta_attune = 1 + ((1.0 * (caster_attune - target_attune)) / stats.MAX_STAT)
        scaled_dam = base_dam * delta_attune
        scale = random.randint(9,11)
        damage = math.trunc((scale * scaled_dam) / 10)
        damages.append(damage)
    return damages

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
    if (level_rand * mind_scale) > uncontrolled_thresh:
        if random.random() < cost_fraction:
            return UNCONTROLLED, cost * 2
        else:
            if scales:
                return POWER_CAST, (3 * cost) / 2
            else:
                return FULL_CAST, cost
    elif (level_rand * mind_scale) > power_thresh:
        if scales:
            return POWER_CAST, (3 * cost) / 2
        else:
            return FULL_CAST, cost
    elif (level_rand * mind_scale) > normal_thresh:
        return FULL_CAST, cost
    elif (level_rand * mind_scale) >  half_thresh:
        if scales:
            return HALF_EFFECT, (3 * cost) / 4
        else:
            return FIZZLE, cost / 4
    else:
        return FIZZLE, cost / 4


def simulate_cast(caster, spell, cst_levels=None, spell_levels=None, samples=100):
    results = []
    for level in range(1,100):
        this_level = []
        cst_level = None
        spell_level = None
        if cst_levels is None:
            cst_level = mobs.stats_of_level(caster, level)
        else:
            cst_level = skill.scale_by_level(caster, cst_levels[level])
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
            val,cost = use_skill_spell(cst_level, spell_level)
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
            atk_level = mobs.stats_of_level(attack, level)
        else:
            atk_level = mobs.stats_of_level(attack, atk_levels[level])
        if trg_levels is None:
            trg_level = mobs.stats_of_level(target, level)
        else:
            trg_level = mobs.stats_of_level(target, trg_levels[level])
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
        print level, "\tmiss\t", miss_count, "\tglance\t", glance_count, "\thit\t", hit_count,"\tcrit\t", crit_count
        results.append(this_level)
    return results    

def setup_combat_order(party, enemies):
    order_scores = []
    # roll for the party
    for ind in range(0,len(party)):
        pmem = party[ind]
        rec = { 'side' : 'party',
                'index' : ind,
                'score' : get_combat_action_score(pmem) }
        order_scores.append(rec)
    # roll for the enemy
    for ind in range(0,len(enemies)):
        pmem = enemies[ind]
        rec = { 'side' : 'enemies',
                'index' : ind,
                'score' : get_combat_action_score(pmem) }
        order_scores.append(rec)
    order_scores.sort(key = lambda el : el['score'])
    order_scores.reverse()
    return order_scores

def random_alive(team):
    alive = []
    for mem in team:
        if mem['current_hp'] > 0:
            alive.append(mem)
    return random.choice(alive)

def select_action(actor, targets, teammates):
    """ Use mild intelegence to select action"""
    action = None
    target = None
    if actor['current_ap'] > 0:
        team_ind = -1
        for teammate in teammates:
            team_ind += 1
            percent = (1.0 * teammate['current_hp']) / teammate['max_hp']
            if percent <= 0.25:
                return team_ind, 'HEAL'
    # haven't healed, roll dice on skill vs attack
    action_rand = random.random()
    min_ind = None
    min_hp = None
    ind = -1
    for target in targets:
        ind += 1
        if min_hp is None:
            min_hp = target['current_hp']
            min_ind = ind
        elif min_hp < target['current_hp'] and target['current_hp'] > 0:
            min_hp = target['current_hp']
            min_ind = ind
    if action_rand > 0.2 or actor['current_ap'] <= 0: #skill attack
        return min_ind, 'PHYS-ATTACK'
    else:
        return min_ind, 'SKILL-ATTACK'

def considered_action(actor, targets, teammates, affil_string):
    target_ind, selected = select_action(actor, targets, teammates)
    dmg_sum = 0
    if selected == 'HEAL':
        trgs = [teammates[target_ind]]
        spell = actor['HEAL']
        cast_type, cost = use_skill_spell(actor, spell)
        actor['current_ap'] -= cost
        damages = do_spell_dam(actor, trgs, spell, cast_type)
        for ind in range(0,len(trgs)):
            dmg_sum += damages[ind]
            trgs[ind]['current_hp'] -= damages[ind]
    elif selected == 'SKILL-ATTACK':
        trgs = [targets[target_ind]]
        spell = actor['SKILL-ATTACK']
        cast_type, cost = use_skill_spell(actor, spell)
        actor['current_ap'] -= cost
        damages = do_spell_dam(actor, trgs, spell, cast_type)
        for ind in range(0,len(trgs)):
            dmg_sum += damages[ind]
            trgs[ind]['current_hp'] -= damages[ind]
    elif selected == 'PHYS-ATTACK':
        target = targets[target_ind]
        hit_type = check_hit(actor, target)
        weapon = target['PHYS-ATTACK']
        dam = do_atk_dam(actor, target,
                         weapon['min_dam'], weapon['max_dam'],
                         hit_type)
        dmg_sum += dam
        target['current_hp'] -= dam
    if LOUD:
        print affil_string, "takes action", selected, "doing damage\t", dmg_sum
    return selected

def rand_action(actor, targets, teammates, affil_string):
    avail_actions = [('HEAL', 0.1), ('SKILL-ATTACK', 0.2), ('PHYS-ATTACK', 0.7)]
    action_choice = random.random()
    selected = None
    dmg_sum = 0
    for (action_nm, action_score) in avail_actions:
        if selected is None and action_score > action_choice:
            selected = action_nm
        else:
            action_choice -= action_score
    if actor['current_ap'] < 0:
        selected = 'PHYS-ATTACK'
    if selected == 'HEAL':
        trgs = [random_alive(teammates)]
        spell = actor['HEAL']
        cast_type, cost = use_skill_spell(actor, spell)
        actor['current_ap'] -= cost
        damages = do_spell_dam(actor, trgs, spell, cast_type)
        for ind in range(0,len(trgs)):
            dmg_sum += damages[ind]
            trgs[ind]['current_hp'] -= damages[ind]
    elif selected == 'SKILL-ATTACK':
        trgs = [random_alive(targets)]
        spell = actor['SKILL-ATTACK']
        cast_type, cost = use_skill_spell(actor, spell)
        actor['current_ap'] -= cost
        damages = do_spell_dam(actor, trgs, spell, cast_type)
        for ind in range(0,len(trgs)):
            dmg_sum += damages[ind]
            trgs[ind]['current_hp'] -= damages[ind]
            
    elif selected == 'PHYS-ATTACK':
        target = random_alive(targets)
        hit_type = check_hit(actor, target)
        weapon = target['PHYS-ATTACK']
        dam = do_atk_dam(actor, target,
                         weapon['min_dam'], weapon['max_dam'],
                         hit_type)
        dmg_sum += dam
        target['current_hp'] -= dam
    if LOUD:
#        print affil_string, actor['label'], "takes action", selected, "doing damage\t", dmg_sum
        print affil_string, "takes action", selected, "doing damage\t", dmg_sum
    return selected
            

def check_alive(char):
    return char['current_hp'] > 0
        
def check_dead(char_list):
    for char in char_list:
        #some character is alive
        if check_alive(char):
            return False
    return True

def run_combat_phase(party, enemies):
    order = setup_combat_order(party,enemies)
    repeat = False
    enemy_actions = 0
    party_actions = 0
    while True:
        repeat = False
        for step in order:
            if check_dead(party):
                if LOUD:
                    print "Party dead, exiting"
                return party_actions, enemy_actions
            if check_dead(enemies):
                if LOUD:
                    print "Enemies dead, exiting"
                return party_actions, enemy_actions
            if step['score'] > 0:
                if step['side'] == 'party':
                    actor = party[step['index']]
                    if not check_alive(actor):
                        step['score'] = 0
                    else:
                        party_actions += 1
                        considered_action(actor, enemies, party, "Party")
                        step['score'] -= DEFAULT_ACTION_COST
                        repeat = True
                else:
                    actor = enemies[step['index']]
                    if not check_alive(actor):
                        step['score'] = 0
                    else:
                        enemy_actions += 1
                        considered_action(actor, party, enemies, "Enemy")
                        step['score'] -= DEFAULT_ACTION_COST
                        repeat = True
        if not repeat:
            return party_actions, enemy_actions

def reset_char(char):
    char['current_hp'] = char['max_hp']
    char['current_ap'] = char['max_ap']

def reset_party(party):
    for mem in party:
        reset_char(mem)
        
def run_combat(party, enemies, at_level = None, max_turns = 100):    
    if at_level:
        party = mobs.party_of_level(party, at_level)
        enemies = mobs.party_of_level(enemies, at_level)
    initial_ap = 0
    initial_hp = 0
    for pmem in party:
        initial_ap += pmem['current_ap']
        initial_hp += pmem['current_hp']
    party_dead = False
    enemy_dead = False
    turn = -1
    party_actions = 0
    enemy_actions = 0
    while not (party_dead or enemy_dead) and turn < max_turns:
        turn += 1
        if LOUD:
            print "Starting turn", turn 
        pact, eact = run_combat_phase(party, enemies)
        party_actions += pact
        enemy_actions += eact
        party_dead = check_dead(party)
        enemy_dead = check_dead(enemies)

    final_ap = 0
    final_hp = 0
    for pmem in party:
        final_ap += pmem['current_ap']
        final_hp += pmem['current_hp']
    return { 'party_survives': not party_dead,
             'hp_cost' : initial_hp - final_hp,
             'ap_cost' : initial_ap - final_ap,
             'turns' : turn,
             'party_actions' : party_actions,
             'enemy_actions' : enemy_actions,
    }

def sample_combat(party, enemies, samples=500, at_level=None):
    data = []
    while samples > 0:
        reset_party(party)
        reset_party(enemies)
        data.append(run_combat(party, enemies, at_level=at_level))
        samples -= 1
    return data


def main():
    hero_phys = chars.hero(stats.MENTAL, stats.FINESSE)
    hero_fin = chars.hero(stats.MENTAL, stats.PHYSICAL)
    hero_mnt = chars.hero(stats.FINESSE, stats.PHYSICAL)
    party = [hero_fin, hero_phys, hero_mnt]
    results = sample_combat(party, mobs.tough_decent, samples=1, at_level=75)
    print results
    
    
if __name__ == '__main__':
    main()
