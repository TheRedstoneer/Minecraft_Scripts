# Minecraft Scripts

These are some scripts I made to make my life a bit easier.
python3 required to run.

#### Let's go over them:
- ##### create_datapack

  It creates a bare datapack-folder-structure with some basic files.

- ##### get_scoreboards \<World Folder\>

  since Mojang removed a _very_ useful feature to list all scoreboards with their type (e.g. killCount, dummy),
  this little tool prints them out.

- ##### create_trigger_adv

  It creates an Advancement that triggers a function, if a player enters a region.
  The region is being set from the current player position (from level.dat).
  1. (in MC) Stand in the center of your desired region and press ESC
  2. run the script. It prints your current position.
  3. enter the function you want to execute, eg. "setup:event"
  4. The tool generated the advancement file "advancements/setup/event.json" and the function "setup/functions/event.mcfunction"
  5. (in MC) /reload the datapack you should see a "function triggered!" in the chat!
  6. it only triggers once. you can reset it by executing: "/advancement revoke @a only setup:event"


- ##### diff

  self-made diff tool, since the git diff only compares lines. this tool shows you the modified chars. So it only makes sense if you made some tiny changes that you cannot spot.

- ##### create_model_json

  This script generates a predicate-override file for items. With these files, you can display multiple models using just one item!
  There are two options:
  1. Damage-Values
  Pretty cool for survival, so a tool can break visually too.
  for this, you need to set `USE_CMD = False`
  This is not recommended for other models (eg. in adventuremaps)
  2. CustomModelData
  This

  ###### How to use:
  create a .model file with a valid mc-name (I'll use `diamond_hoe.model`) in the `models/item` directory. Here you can write down all the paths-to-the-model, eg. write `npc/body/head` when the model-file is saved in `models/npc/body/head.json`.
  The line-number corresponds to the ID used in game. so if your model is on line 6, use `CustomModelData:6` to load it. You can use # as a comment, so this line won't be generated!

  execute the python-script in the `models/item` directory, every corresponding json-file will be generated.

- ##### anim_texture
  This generates an animated texture (like a gif) with an overlay-img from n source-images.
  You can find more information and set all the params in the source.
