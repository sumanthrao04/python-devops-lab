import os
print(os.getcwd())

import platform
print(f"operating system :  {platform.system()}")
print(f"OS release : {platform.release()}")
print(f"Architecture : {platform.machine()}")

from platform import system

print(system())