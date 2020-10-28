#/bin/python3

import os
import sys
from shutil import copytree
import json

versions = [13,14,16]

start_str="""
--------------------------------
        Datapack Generator
        by TheRedstoneer
--------------------------------
"""
def touch(path):
    open(path, "w").close()

def copy_tags(target_path):
    tag_path = "minecraft16/resourcepacks/vanilla/tags"
    copytree(tag_path, target_path+"/tags")


def getDirs(dir,name):
    ll = list()
    i = 0
    for f in os.listdir(dir):
        if(os.path.isdir(os.path.join(dir,f)) and name.lower() in f.lower()):
            i+=1
            print(f"- {f} [{i}]")
            ll.append(f)
    return ll

def intinput(max):
    try:
        num = int(input())
    except:
        num = 0
    while(num == 0 or num > max):
        print("no valid input!")
        try:
            num = int(input())
        except:
            num = 0
    return num

####################################################################
def create_mcmeta(path,version,text):
    mcmeta = dict()
    mcmeta["pack"] = dict()
    mcmeta["pack"]["pack_format"] = 4 if version < 16 else 6
    mcmeta["pack"]["description"] = text
    with open(os.path.join(path,"pack.mcmeta"),"w") as packfile:
        packfile.write(json.dumps(mcmeta))

def create_tagfile(name,path,function):
    tag = dict()
    tag["values"] = list()
    tag["values"].append(function)
    with open(os.path.join(path,name+".json"),"w") as tagfile:
        tagfile.write(json.dumps(tag))
####################################################################

def createDatapack(path,version,name,files):
    create_mcmeta(path,version,name+" Datapack!")

    if version >= 16:
        work_folder = os.path.join(path,"data/minecraft/")
        os.makedirs(work_folder)
        copy_tags(work_folder)
        work_folder = os.path.join(path,"data/minecraft/tags/functions")
    else:
        work_folder = os.path.join(path,"data/minecraft/tags/functions")
        os.makedirs(work_folder)

    # minecraft tick tags
    if files[0]: create_tagfile("tick", work_folder, name+":"+files[0])
    if files[1]: create_tagfile("load", work_folder, name+":"+files[1])

    #functions in own namespace
    work_folder = os.path.join(path,"data/"+name+"/functions")
    os.makedirs(work_folder)
    if files[0]: touch(os.path.join(work_folder,files[0]+".mcfunction"))
    if files[1]: touch(os.path.join(work_folder, files[1]+".mcfunction"))

os.chdir("..")
curr_path = os.getcwd()
print(start_str)
print("which mc version?")
#folder_poss = getDirs(curr_path,"minecraft")
#read number 12-16
version = intinput(16)
mpath = "minecraft"+str(version)


curr_path += os.path.sep + mpath+ os.path.sep + "saves"
world_cnt = len(os.listdir(curr_path))
if world_cnt == 0: #no world in folder -> error and exit
    print("No world found.")
    sys.exit(1)
if world_cnt > 1:
    search = input("Search for world: ")
    folder_poss = getDirs(curr_path,search)
    #no world found in search -> search new
    if len(folder_poss) == 0:
        print("No world found.")
        while(len(folder_poss) == 0):
            search = input("Search for world: ")
            folder_poss = getDirs(curr_path,search)
    #Search found just one world
    elif len(folder_poss) == 1:
        world = folder_poss[0]
    else: #multiple possible worlds found
        num = intinput(len(folder_poss)-1)
        world = folder_poss[num-1]
else: #just found exactly one world
    world = os.listdir(curr_path)[0]

print(f"Selected world \"{world}\"")
curr_path += os.path.sep + world + os.path.sep + "datapacks"

datapack_name = input("Name of the new Datapack: ")
while(datapack_name[0].isdigit()):
    print("The first char cannot be a digit!")
    datapack_name = input()
if os.path.isdir(os.path.join(curr_path,datapack_name)):
    print("This datapack already exists.\n(if you want to generate the subfolders, you have to delete this folder!)")
    sys.exit(2)
curr_path += os.path.sep + datapack_name
print(curr_path)

loop_file = input("name of the main looping mcfunction (or leave empty): ")
reset_file = input("name of the load mcfunction (or leave empty): ")
if loop_file == "": loop_file = None
if reset_file == "": reset_file = None

os.makedirs(curr_path)

createDatapack(curr_path, version,datapack_name,(loop_file,reset_file))
