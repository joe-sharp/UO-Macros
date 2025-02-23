# Name: Herding and Tracking
# Description: Train Harding and Tracking at the same time. Periodically you will need to herd more difficult creatures.
# Author: Telfer
# Shard: UOA
# Date: Tue Feb 11 2025

def herd():
    UseObject(0x40098035)
    WaitForTarget(5000)
    Target('last')
    WaitForTarget(5000)
    TargetTileOffset(0, 0, 0)

def track():
    UseSkill('Trackin')
    WaitForGump(0xb16e7d71, 5000)
    ReplyGump(0xb16e7d71, 5)

def eat_and_drink():
    UseObject(0x4001da02)
    UseObject(0x4001cdf5)

for i in range(20):
    herd()
    track()

eat_and_drink()