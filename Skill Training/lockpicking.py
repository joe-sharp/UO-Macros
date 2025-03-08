# Use the LOOKUP and set to your level rounded down
# must be 10-90
level = 50
SetQuietMode(True)
CONTAINER_TYPE = 0x9AA
LOOKUP = {
    10: 'Dilapidated Lockpicking Chest',
    20: 'Broken Lockpicking Chest',
    30: 'Rusted Lockpicking Chest',
    40: 'Corroded Lockpicking Chest',
    50: 'Passable Lockpicking Chest',
    60: 'Average Lockpicking Chest',
    70: 'Competent Lockpicking Chest',
    80: 'Hard Lockpicking Chest',
    90: 'Harder Lockpicking Chest'
}

def PrepareContainers():
    containers = []
    # Need to clear the list or the gump will only work once
    ClearIgnoreList()
    # Get nearby containers on ground
    while FindType(CONTAINER_TYPE, 2):
        containers.append(GetAlias('found'))
        IgnoreObject('found')
    return sorted(containers, key=lambda id: Name(id))
boxes = PrepareContainers()

def SetLockpickBox(level):
    for box in boxes:
        if Name(box) == LOOKUP[level]:
            SetMacroAlias('box', box)

while Skill("Lockpickin") < SkillCap("Lockpickin"):
    SetLockpickBox(level)
    if not FindType(0x14fc, 0, 'backpack'):
        HeadMsg("cant find lockpick, script stoped", "self")
        Stop()
    if Skill("Lockpickin") > 10:
        level = 10
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 20 and level == 10):
        level = 20
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 30 and level == 20):
        level = 30
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 40 and level == 30):
        level = 40
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 50 and level == 40):
        level = 50
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 60 and level == 50):
        level = 60
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 70 and level == 60):
        level = 70
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 80 and level == 70):
        level = 80
        SetLockpickBox(level)
    if (Skill("Lockpickin") > 90 and level == 80):
        level = 90
        SetLockpickBox(level)
    
    UseType(0x14fc)
    WaitForTarget(5000)
    Target('box')
    Pause(1000)
Msg('[emote woohoo')