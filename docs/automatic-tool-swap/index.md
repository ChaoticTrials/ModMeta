# Automatic Tool Swap
[![](https://badges.moddingx.org/modrinth/downloads/automatic-tool-swap?style=flat)](https://modrinth.com/mod/automatic-tool-swap)
[![](https://badges.moddingx.org/curseforge/downloads/361977?style=flat)](https://www.curseforge.com/minecraft/mc-mods/automatic-tool-swap)
[![](https://img.shields.io/github/issues-raw/ChaoticTrials/ToolSwap?style=flat-square)](https://github.com/ChaoticTrials/ToolSwap)

## Config

### sneak_to_prevent
- **Default:** `true`
- **Description:** If enabled, sneaking prevents tool swapping.

```properties
sneak_to_prevent=true
```

### sorttype
- **Default:** `LEVEL`
- **Description:** Sets the mode for tool selection:
    - `LEVEL`: Sorted by harvest level, lowest first
    - `LEVEL_INVERTED`: Sorted by harvest level, highest first
    - `LEFT_TO_RIGHT`: Sorted from left to right
    - `RIGHT_TO_LEFT`: Sorted from right to left
    - `ENCHANTED_FIRST`: Sorted by harvest level, highest enchanted item first
    - `ENCHANTED_LAST`: Sorted by harvest level, highest unenchanted item first

Allowed Values: `LEVEL`, `LEVEL_INVERTED`, `LEFT_TO_RIGHT`, `RIGHT_TO_LEFT`, `ENCHANTED_FIRST`, `ENCHANTED_LAST`

```properties
sorttype="LEVEL"
```

### save
- **Default:** `false`
- **Description:** If enabled, tools with 1 durability left will be saved. This only applies to breaking a block and
  does not affect actions like stripping, flattening, or tilling.

```properties
save=true
```

### min_durability
- **Default:** `1`
- **Range:** `> 1`
- **Description:** Minimum durability an item must have to be saved.

```properties
min_durability=1
```

### ignore_harvest_level
- **Default:** `true`
- **Description:** If enabled, the harvest level of tools will be ignored when breaking blocks. Otherwise, it will
  always use the lowest possible tool.

```properties
ignore_harvest_level=false
```

## Showcase

{yt_video}
