GOAL = 100
last = 50

if not FindAlias('Pouch'):
    PromptAlias('Pouch')

while Skill('Stealin') < GOAL:
    for i in range(20):
        UseSkill('Stealin')
        WaitForTarget(5000)
        if FindType(0x4ccd, 0, 'Pouch'):
        	Target('found')
        Pause(1000)
        Organizer('steal')
        Pause(3000)
    PlayMacro('eat')
    Pause(1000)

    if (Skill('Stealin') >= 60 and Skill('Stealin') < 70 and last == 50):
        Organizer('10feathers')
        last = 60
    if (Skill('Stealin') >= 70 and Skill('Stealin') < 80 and last == 60):
        Organizer('10feathers')
        last = 70
    if (Skill('Stealin') >= 80 and Skill('Stealin') < 90 and last == 70):
        Organizer('10feathers')
        last = 80
    if (Skill('Stealin') >= 90 and Skill('Stealin') < 100 and last == 80):
        Organizer('10feathers')
        last = 90
    if (Skill('Stealin') >= 100 and Skill('Stealin') < 110 and last == 90):
        Organizer('10feathers')
        last = 100
    if (Skill('Stealin') >= 100 and Skill('Stealin') < 110 and last == 100):
        Organizer('10feathers')
        last = 110
    