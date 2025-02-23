GOAL = 100

while Skill('Inscriptio') < GOAL:
    PlayMacro('eat')
    Organizer('Regs')
    if Mana('self') < 50:
    	UseSkill('Meditatio')
    if Skill('Inscriptio') < 55:
		UseType(0x2051)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 22)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 51)
		WaitForGump(0x38920abd, 5000)
    if (Skill('Inscriptio') >= 55 and Skill('Inscriptio') < 65):
		UseType(0x2051)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 29)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 16)
		WaitForGump(0x38920abd, 5000)
    if (Skill('Inscriptio') >= 65 and Skill('Inscriptio') < 85):
		UseType(0x2051)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 36)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 51)
		WaitForGump(0x38920abd, 5000)
    if (Skill('Inscriptio') >= 85 and Skill('Inscriptio') < 94):
		UseType(0x2051)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 43)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 16)
		WaitForGump(0x38920abd, 5000)
    if (Skill('Inscriptio') >= 94 and Skill('Inscriptio') < 100):
		UseType(0x2051)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 50)
		WaitForGump(0x38920abd, 5000)
		ReplyGump(0x38920abd, 16)
		WaitForGump(0x38920abd, 5000)
    if (Skill('Inscriptio') >= 100 and Skill('Inscriptio') < 120):
        # TBD
        Stop()

