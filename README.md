# RPR-CombatSim
Python based combat simulator for role-playing racer
Meant to hammer out the ideas behind combat, do balance.

## Why Python
It's real close to GML.  It has a repl.  I know it.

## Why not do it in the code directly
I want to do thousands of automated combats to see outcomes.  I want
to iterate fast.  I want to generate graphs showing outcome.  GML
doesn't lend itself to any of that.  A second program to test the
ideas seems like the best possible fit.

## How far do you need to go
Just shy of naming abilities.  You probably don't need fire, ice,
wind.  You need the notion of strong againts / weak to to check out
balance.

# Setup
## What to Install
python
python-pip
libtk-img libtk-imgdev
python-tk
pip via pip, python -m pip install -U pip
matplotlib via pip, python -m pip install -U matplotlib

# Repository layout
Everything is flat in src

# Running the Simulator
## python plot_derived_stats.py
	show me the stats associated with each class of character by level
## python plot_combat_vals.p
	show me turn order information by level
## python weapon.py
	show me weapon damage by level

## python combat_explorer
	Simulate combat and show results

# Contributors
Seabass what for writing this mess
Steve for the idea of rolling out the sim in the first place
