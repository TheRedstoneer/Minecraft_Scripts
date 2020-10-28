# Minecraft Scripts

These are some scripts I made to make my live a bit easier.

#### Let's go over them:
- create_datapack

  It creates a bare datapack-folder-structure with some basic files.

- get_scoreboards \<World Folder\>

  since Mojang removed a _very_ useful feature to list all scoreboards with their type (e.g. killCount, dummy),
  this little tool prints them out.

- create_trigger_adv

  It creates an Advancement that triggers a function, if a player enters a region.
  The region is being set from the current player position (from level.dat).
  1. (in MC) Stand in the center of your desired region and press ESC
  2. run the script. It prints your current position.
  3. enter the function you want to execute, eg. "setup:event"
  4. The tool generated the advancement file "advancements/setup/event.json" and the function "setup/functions/event.mcfunction"
  5. (in MC) /reload the datapack you should see a "function triggered!" in the chat!
  6. it only triggers once. you can reset it by executing: "/advancement revoke @a only setup:event"


- diff

  selfmade diff tool, since the git diff only compares lines. this tool shows you the modified chars. So it only makes sense if you made some tiny changes that you cannot spot.

-
