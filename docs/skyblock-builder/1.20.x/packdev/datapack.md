# Datapacks
## Loot Item Function
With implementing [spreads](packdev.md#configuring-templates), you can also create maps which show the destination of
each spread for this team. Use it like this in loot tables:
```json5
{
  "type": "minecraft:item",
  "name": "minecraft:map",
  "functions": [
    {
      "spreads": "spread_1", // file name without extension, case-sensitive
      "decoration": "red_x", // "red_x" is default if none is set
      "function": "skyblockbuilder:spread_map",
      "zoom": 2 // 2 is default if none is set
    },
    // these are just two examples, don't combine them
    {
      "spreads": [ // can be an array, too
        "spread_1",
        "spread_2"
      ],
      "decoration": "red_x", // "red_x" is default if none is set
      "function": "skyblockbuilder:spread_map",
      "zoom": 2 // 2 is default if none is set
    }
  ]
}
```