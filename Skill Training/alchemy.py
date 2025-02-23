GOAL = 100

while Skill('Alchem') < GOAL:
    PlayMacro('eat')
    Organizer('Regs')
    if Skill('Alchem') < 45:
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 135)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 45 and Skill('Alchem') < 55):
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 184)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 55 and Skill('Alchem') < 65):
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 142)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 65 and Skill('Alchem') < 75):
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 191)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 75 and Skill('Alchem') < 85):
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 149)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 85 and Skill('Alchem') < 95):
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 58)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 95 and Skill('Alchem') < 100):
        UseType(0x4ce9)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 1)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 156)
        WaitForGump(0x38920abd, 5000)
    if (Skill('Alchem') >= 100 and Skill('Alchem') < 120):
        # TBD
        Stop()

