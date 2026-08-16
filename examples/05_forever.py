"""Using forever().

Stop this program with Ctrl+C.
"""

from beyondblocks import forever, wait

def heartbeat():
    print("Program is still running...")
    wait(1)

forever(heartbeat)
