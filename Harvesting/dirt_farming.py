length = 20
width = 17

for i in range(width):
    for i in range(length):
        Walk('East')
        Pause(1000)
    Turn('South')
    Walk('South')
    Turn('West')
    for i in range(length):
        Walk('West')
        Pause(1000)
    Turn('South')
    Walk('South')
    Turn('East')
