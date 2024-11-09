import os
import random
from sys import argv

def get_cmds():
    commands = set()
    for path in os.getenv("PATH", "").split(os.pathsep):
        if os.path.isdir(path):
            for cmd in os.listdir(path):
                full_path = os.path.join(path, cmd)
                if os.access(full_path, os.X_OK) and not os.path.isdir(full_path):
                    commands.add(cmd)
    return sorted(commands)

commands = (get_cmds()) 
random.shuffle(commands)
if len(commands)%2 != 0:
    commands.pop(0)

i = 0
j = int(len(commands)/2)

filePath = argv[1]
if (input(f"{filePath}: File Path given, you sure bud? [y/n] ").lower().replace(" ", "")) == "y":
    pass
else:
    print("Quiting...")
    exit()

with open(filePath, "w") as f:
    while i < len(commands)/2:
        t = f"alias {commands[i]}=\"{commands[j]}\"\n"
        f.writelines(t)
        i+=1
        j+=1

