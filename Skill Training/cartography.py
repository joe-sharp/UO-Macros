GOAL = 99.5

while Skill("Cartograph") < GOAL:
    PlayMacro('eat')
    if Skill("Cartograph") < 65:
        UseType(0x2052)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 9)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Cartograph") >= 65 and Skill("Cartograph") < 70):
        UseType(0x2052)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 16)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Cartograph") >= 70 and Skill("Cartograph") < 85):
        UseType(0x2052)
        WaitForGump(0x38920abd, 5000)
        ReplyGump(0x38920abd, 23)
        WaitForGump(0x38920abd, 5000)
    if (Skill("Cartograph") >= 85 and Skill("Cartograph") < 93):
		UseType(0x2052)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 30)
		WaitForGump(0x38920abd, 5000)
    if (Skill("Cartograph") >= 93 and Skill("Cartograph") < 99.5):
		UseType(0x2052)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 37)
		WaitForGump(0x38920abd, 5000)
