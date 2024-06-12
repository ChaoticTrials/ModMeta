# Dimensions
*The config values on this page can be found in `config/skyblockbuilder/dimensions.json5`*

## Overworld
Here you can set if the overworld should generate as in a normal world. This will ignore the configured 
[structures](structures.md#generating-structures) and [features](structures.md#generating-features). This is useful when
your [starting dimension](spawn.md#dimension) is not the overworld.

## The Nether
Here you can set if the nether should generate as in a normal world. This will ignore the configured 
[structures](structures.md#generating-structures) and [features](structures.md#generating-features).

You can also set a structure for a nether portal. This is a `.nbt` or `.snbt` file within the directory 
`config/skyblockbuilder/templates` and must contain at least one nether portal block. This will be generated whenever
no nether portal was found in the nether, so be careful with valuable content - users can destroy the portal and
re-generate this template over and over again.

## The End
Here you can set if the end should generate as in a normal world. This will ignore the configured 
[structures](structures.md#generating-structures) and [features](structures.md#generating-features). Additionally, you
can choose if the main island (with the dragon) should be generated or not.

## Other dimensions
All other dimensions (added by datapacks, or other mods) will not be void and can't be configured. If you want
compatability, ask the mod author of this mod or [open an issue on GitHub 🔗](https://github.com/MelanX/SkyblockBuilder/issues/new?assignees=MelanX&labels=enhancement&template=feature_request.md&title=).