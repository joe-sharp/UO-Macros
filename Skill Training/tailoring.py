GOAL = 100

while Skill("Tailorin") < GOAL:
    # if Skill("Tailorin") < 35:
        # TBD - Short Pants
    # if (Skill("Tailorin") >= 35 and Skill("Tailorin") < 42):
        # TBD - Full Apron
    # if (Skill("Tailorin") >= 42 and Skill("Tailorin") < 50):
        # TBD - Cloaks
    if (Skill("Tailorin") >= 50 and Skill("Tailorin") < 54):
        UseType(0xf9f)
        WaitForTarget(5000)
        TargetType(0x2783)
        UseType(0x4c81)
        # Fill in gump picks for Female Kimono
    if (Skill("Tailorin") >= 54 and Skill("Tailorin") < 65):
        UseType(0xf9f)
        WaitForTarget(5000)
        TargetType(0x1f03)
        UseType(0x4c81)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 15)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 86)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Tailorin") >= 65 and Skill("Tailorin") < 72):
        UseType(0xf9f)
        WaitForTarget(5000)
        TargetType(0x2798)
        UseType(0x4c81)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 8)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 163)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Tailorin") >= 72 and Skill("Tailorin") < 78):
        UseType(0xf9f)
        WaitForTarget(5000)
        TargetType(0x2797)
        UseType(0x4c81)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 36)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 16)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Tailorin") >= 78 and Skill("Tailorin") < 110):
        UseType(0xf9f)
        WaitForTarget(5000)
        TargetType(0x175d)
        UseType(0x4c81)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 29)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 58)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Tailorin") >= 110 and Skill("Tailorin") < 115):
        # TBD
        UseType(0x4c81)
        WaitForGump(0x38920abd, 5000)
        Stop()
    if (Skill("Tailorin") >= 115 and Skill("Tailorin") < 120):
        # TBD
        UseType(0x4c81)
        WaitForGump(0x38920abd, 5000)
        Stop()
