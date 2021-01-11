
import os
import sys
import json

#if you want to use classic damage-values (=False) or the "new" custom_model_data tag (=True)
USE_CMD = True
# (only if USE_CMD = False) set to True if you want to hide the damage-bar
UNBREAKABLE = False

DMG_VALS = {"wooden":59, "stone": 131, "iron": 250, "golden": 32, "diamond": 1561, "netherite": 2031, "carrot_on_a_stick": 26}

def create_dict(name):
    model = dict()
    model["__comment"] = "Model made by TheRedstoneer"
    model["parent"] = "item/handheld"
    model["textures"] = {"layer0": "item/"+name}

    return model

#Creates one damage entry
def create_damage(model_name, damage_V):
    damage = dict()
    damage["predicate"] = dict()
    damage["predicate"]["damaged"] = 0 if UNBREAKABLE else 1
    damage["predicate"]["damage"] = damage_V
    damage["model"] = model_name
    return damage

def create_model_data(model_name, index):
    cmd = dict()
    cmd["predicate"] = dict()
    cmd["predicate"]["custom_model_data"] = index
    cmd["model"] = model_name
    return cmd

def get_max_dmg(model_file):
    for item_type in DMG_VALS.keys():
        if(model_file.startswith(item_type)):
            return DMG_VALS[item_type]

def create_file(name, max_dmg):
    with open(name+".model","r") as model_f, open(name+".json","w") as json_f:
        #create Header
        modelDict = create_dict(name)
        model_list = list()
        x = 0

        for model in model_f:
            x+=1
            if model.startswith("#"): continue
            if USE_CMD:
                model_list.append(create_model_data(model[:-1],x))
            else:
                model_list.append(create_damage(model[:-1], round(x/max_dmg, 12)))
        modelDict["overrides"] = model_list #put list in dict

        #finally writing everything into file
        json.dump(modelDict, json_f, indent=4)

#general path

#os.chdir(os.path.dirname(__file__))
for model_file in os.listdir():
    if(model_file.endswith(".model")):
        model_file = model_file[:-6] #get name w/out ".model"
        print("> "+model_file)
        create_file(model_file, (None if USE_CMD else get_max_dmg(model_file)))
