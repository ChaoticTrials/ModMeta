# World
*The config values on this page can be found in `config/skyblockbuilder/world.json5`*

## Island distance
The distance between two islands. If you choose `minecraft:the_nether` as [start dimension](spawn.md#dimension), it will be 
divided by 8.

## Offset
The offset from 0, 0, 0 to generate the islands. Can be used to generate them in the middle of .mca files, or moving
the island up/down. The value in the middle is you height, one and three is for x and z direction.

## Sea height
The sea level in the world. This has nothing to do with the water height in the world. This does affect the spawn height
of squids for example.

## Surface
The block settings for generating the different dimensions surfaces. It's in the same format as 
[flat world generation settings 🔗](https://minecraft.fandom.com/wiki/Superflat#Preset_code_format), but will ignore
the biome. You can set it for each dimension. Instead of removing the dimension from the list, just set it to an empty
string to generate it completely void. If the surface is disabled, it will ignore the setting.

## Biomes
It's a map which provides [ResourceLists 🔗](https://moddingx.org/libx/org/moddingx/libx/util/data/ResourceList.html#use_resource_lists_in_configs).
It's set to allow all biomes per default. You can deny biomes by adding them to the list. Setting `allow_list` to true
will only use the biomes in the list. Keep in mind that each dimension needs at least one valid biome!

A list with all possible structures can be found in `config/skyblockbuilder/data/biomes.txt`.

## Prevent scheduled ticks
This is used to prevent gravel or sand from falling when generating the island. To define which blocks will be
prevented, use the block tag `skyblockbuilder:prevent_scheduled_tick`. This is filled with fallable blocks by default.
This includes all sand, gravel, and concrete powder types, as well as any anvil, pointed dripstone, and the dragon egg.

## Leave to Overworld
This can be enabled if the overworld is still normal, and maybe there's no spawn. This will force the player to be
teleported to the overworld world spawn instead of the default spawn.