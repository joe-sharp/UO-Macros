SetQuietMode(True)
CONTAINER_TYPE = 0xE76

def PrepareContainers():
    containers = []
    # Need to clear the list or the gump will only work once
    ClearIgnoreList()
    # Get nearby containers on ground
    while FindType(CONTAINER_TYPE, 2):
        containers.append(GetAlias('found'))
        IgnoreObject('found')
    return sorted(containers, key=lambda id: Name(id))
containers = PrepareContainers()

selected = ItemArrayGump(containers, True, 200, 200)[0]
UseObject(selected)