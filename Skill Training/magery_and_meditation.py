# Name: Training Magery
# Description: Train magery skill until the goal you want. Modified from a macro by Lissandro
# Author: Telfer
# Shard: UOA
# Date: Tue Feb 11 2025


GOAL = 100

while Skill('Mager') < GOAL:
    if Mana('self') < 50:
        # Replace this with a Macro that eats and drinks whatever you want and ends with a `Pause(1000)`.
        # Or simply remove it if you don't need to eat/drink.
        PlayMacro('eat')
        while Mana('self') < MaxMana('self'):
            UseSkill('Meditatio')
            Pause(10000)

    if Skill('Mager') < 45:
        Cast('Bless', 'self')
        Pause(1800)
    if Skill('Mager') >= 45 and Skill('Mager') < 55:
        Cast('greater heal', 'self')
        Pause(2100)
    if Skill('Mager') >= 55 and Skill('Mager') < 65:
        Cast('Poison Field', 'self')
        Pause(2400)
    if Skill('Mager') >= 65 and Skill('Mager') < 75:
        Cast('Invisibility', 'Self')
        Pause(2700)
    if Skill('Mager') >= 75 and Skill('Mager') < 90:
        Cast('Mass Dispel', 'Self')
        Pause(3000)
    if Skill('Mager') >= 90 and Skill('Mager') < 120:
        Cast('earthquake')
        Pause(3300)
