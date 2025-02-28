state_machine = True

while Skill('Ninjits') < 85:
	if Mana('self') < 15:
		UseSkill('Meditatio')
		Pause(10000)
	Cast("Shadowjump")
	WaitForTarget(5000)
	if state_machine:
		TargetTileOffset(0, 5, 0)
	else:
		TargetTileOffset(0, -5, 0)
	if InJournal('You begin to move quietly.') or InJournal('Target cannot be seen.'):
		ClearJournal()
		state_machine = not state_machine
	if InJournal('You must be in stealth mode to use this ability.'):
		ClearJournal()
		UseSkill('Hidin')
		Pause(5000)
		UseSkill('Stealt')
	PlayMacro('eat')
	Pause(3000)
	
while Skill('Ninjits') < 100:
    PlayMacro('eat')
    Pause(1000)
	WaitForContext(0x401a818a, 0, 5000)
	WaitForTarget(5000)
	Target(0x401a86cc)
	for i in range(10):
		Pause(3000)
		UseObject(0x401a818a)
		WaitForTarget(5000)
		Target(0xa83)

