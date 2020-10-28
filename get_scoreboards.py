from nbt.nbt import NBTFile, TAG_Compound, TAG_List
import os
import sys

def getKoords(mynbt):
    x = str(mynbt["size"][0])[0]
    y = str(mynbt["size"][1])[0]
    z = str(mynbt["size"][2])[0]
    return [x,y,z]

def switchType(key,value, indent):
    if(type(value) is TAG_Compound):
        printCompound(value,indent+1)
    elif(type(value) is TAG_List):
        print(key)
        for v in value:
            switchType(value,v,indent+1)
    else:
        for i in range(indent):
            print("\t",end="")
        print(f"{key}: {value}")

def printCompound(comp, indent):
    data_keys = sorted([x for x in comp])
    for key in data_keys:
        value = comp[key]
        switchType(key,value,indent)

def getObjectives(comp):
    objectives = comp["Objectives"]
    for obj in objectives:
        name = obj["Name"]
        type = obj["CriteriaName"]
        print(f"{name}: {type}")

####################################

if len(sys.argv) < 2:
    print(sys.argv[0]+" <World Folder>")
    sys.exit(1)

folder = os.path.join(os.getcwd(),sys.argv[1])
if not os.path.isdir(folder):
    print(sys.argv[1]+" is not a folder!")
    sys.exit(1)

filename = folder+os.sep+"data"+os.sep+"scoreboard.dat"

nbtfile = NBTFile(filename,'rb')
data = nbtfile["data"]
#printCompound(data,0)
getObjectives(data)
