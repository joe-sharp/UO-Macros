# Name: Training Chivalry
# Description: Train Chivalry skill until the goal you want. Modified from a macro by Lissandro
# Author: Telfer
# Shard: UOA
# Date: Tue Feb 11 2025


GOAL = 100

while Skill('Chivalr') < GOAL:
    if Mana('self') < 50:
        # Replace this with a Macro that eats and drinks whatever you want and ends with a `Pause(1000)`.
        # Or simply remove it if you don't need to eat/drink.
        PlayMacro('eat')
        while Mana() < MaxMana('self'):
            UseSkill('Meditatio')
            Pause(10000)
        Dress('rearm')
        Pause(2000)

    if Skill('Chivalr') < 45:
        Cast('Consecrate Weapon')
        Pause(2400)
    if Skill('Chivalr') >= 45 and Skill('Chivalr') < 60:
        Cast('Divine Fury')
        Pause(2400)
    if Skill('Chivalr') >= 60 and Skill('Chivalr') < 70:
        Cast('Enemy of One')
        Pause(2400)
    if Skill('Chivalr') >= 70 and Skill('Chivalr') < 90:
        Cast('Holy Light')
        Pause(2400)
    if Skill('Chivalr') >= 90 and Skill('Chivalr') < 120:
        Cast('Noble Sacrifice')
        Pause(2400)