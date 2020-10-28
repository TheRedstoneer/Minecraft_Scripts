import sys
import json
import os
from nbt.nbt import NBTFile

RADIUS = 4
LEVELDAT = "../../../../level.dat"
PARENT_ADV = "namespace:root"

def getKoords():
    level = NBTFile(LEVELDAT,'rb')

    x = int(float(str(level["Data"]["Player"]["Pos"][0])))
    y = int(float(str(level["Data"]["Player"]["Pos"][1])))
    z = int(float(str(level["Data"]["Player"]["Pos"][2])))
    print(f"x={x} y={y} z={z}")
    return x,y,z


def createAdvFile(mx,my,mz, function):
    d_x = dict(min=mx-RADIUS, max=mx+RADIUS)
    d_y = dict(min=my-1, max=my+4)
    d_z = dict(min=mz-RADIUS, max=mz+RADIUS)
    pos = dict(x=d_x, y=d_y, z=d_z)

    adv = {
        "__comment": "Made by TheRedstoneer",
        "criteria":
        {
            "theredstoneer":
            {
                "trigger": "minecraft:location",
                "conditions": {"position": pos}
            }
        },
        "rewards": {
        "function": function
        },
        "parent": PARENT_ADV
    }
    jsonObj = json.dumps(adv, indent=4)

    namespace, function = function.split(':')
    adv_filename = "advancements" + os.sep + namespace + os.sep + function.replace("/","_") + ".json"
    with open(adv_filename, "w") as f:
        f.write(jsonObj)
    print(f"Resulting Advancement: {adv_filename}\n  !")

def createFuncFile(function):
    namespace, function = function.split(':')
    path = os.path.abspath(os.path.join("", os.pardir))
    filename = path + os.sep + namespace + os.sep + "functions" + os.sep + function + ".mcfunction"

    with open(filename,"w") as f:

        ## Write your Minecraft functions here!
        f.write("say function triggered!")
        f.write("spawnpoint @s\n")

    print("Function: "+filename)


#################################################
# Get player POS from Level.dat file
x,y,z = getKoords()
print("Player-position: "+str((x,y,z)))

inputString = input("Function to run: ")

createAdvFile(x,y,z, inputString)
createFuncFile(inputString)
