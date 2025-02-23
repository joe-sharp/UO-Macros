# Name: Lumberjack Near Me
# Description: Attempts to chop all trees in a 10x10 area around you
# Author: Bittiez
# Shard: Ruins and Riches
from ClassicAssist.UO.Data import Statics
from ClassicAssist.UO import UOMath
from Assistant import Engine
from System import Convert
import clr
clr.AddReference('System.Core')

def GetNearestTree():
    trees = []
    for x in range(Engine.Player.X-10, Engine.Player.X+10):
        for y in range(Engine.Player.Y-10, Engine.Player.Y+10):
            statics = Statics.GetStatics(Convert.ChangeType(Engine.Player.Map, int), x, y)
            if statics == None:
                continue
            for s in statics:
                if s.Name.Contains('tree'):
                    trees.append({'X': s.X, 'Y': s.Y})
    return trees

def moveToPackAnimal():
    Organizer('LogsToPackMule')

def moveToTree(tree):
    i = 0
    while X('self') <> tree['X'] and Y('self') <> tree['Y']:
        if i >= 3:
            HeadMsg('Pathfinding failed. Skipping tree.', 'self')
            return False
        HeadMsg('*Pathfinding*', 'self')
        Pathfind(tree['X'], tree['Y'], 0)
        Pause(2000)
        i += 1
    return True

def lumberjack():
    while not InJournal('not enough') and not InJournal('can't use an axe'):
        UseLayer('TwoHanded')
        WaitForTarget(1000)
        TargetTileOffsetResource(-1, 0, 0)
        Pause(1100)

Trees = GetNearestTree()
if len(Trees) > 0:
    TotalTrees = len(Trees)
    SysMessage(str(TotalTrees) + ' total trees in queue')
    for tree in Trees:
        tree['X'] += 1
        if moveToTree(tree):
            lumberjack()
            moveToPackAnimal()
            PlayMacro('eat')
            TotalTrees -= 1
            SysMessage(str(TotalTrees) + ' trees left in the queue!')
            ClearJournal()