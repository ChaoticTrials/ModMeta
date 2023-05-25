# Data Trader
[![](https://cf.way2muchnoise.eu/650573.svg?badge_style=flat)](https://www.curseforge.com/minecraft/mc-mods/data-trader) 
[![](https://img.shields.io/modrinth/dt/data-trader?color=00AF5C&label=%E3%85%A4&logo=modrinth&style=flat-square)](https://modrinth.com/mod/data-trader) 
[![](https://img.shields.io/github/issues-raw/MelanX/DataTrader?style=flat-square)](https://github.com/MelanX/DataTrader)

A mod which adds a new trader to the game.

## Defining the trades
### File structure
The trader can receive an ID for a merchant offers "recipe". This is a list of single `merchant offer`s. An example
file could look like this:

```json
{
  "Recipes": [
    {
      "buy": {
        "item": "minecraft:diamond",
        "count": 3
      },
      "buyB": {
        "item": "minecraft:wooden_pickaxe"
      },
      "sell": {
        "item": "minecraft:diamond_pickaxe",
        "nbt": "{Damage:0,Enchantments:[{id:\"minecraft:efficiency\",lvl:2},{id:\"minecraft:unbreaking\", lvl:10}]}"
      },
      "uses": 10,
      "maxUses": 50,
      "rewardExp": false,
      "xp": 0,
      "priceMultiplier": 0.0,
      "specialPrice": 0,
      "demand": 0
    }
  ]
}
```

- This example includes only one merchant offer. The trader will sell the item in `sell`.
- The player needs to provide the item in `buy` and `buyB` to receive the item.
`maxUses` is the amount of times the player can use this trade before the trader needs to restock.
- If `rewardExp` is true, the player will receive 3 to 6 xp points for each trade.
`xp` if the amount of xp the trader receives. Since it's not leveling, it's useless here.
- The `priceMultiplier` calculates the price for the item count in `buy`.
- The `specialPriceDiff` could increase or decrease it.
- The `demand` will also calculate the price for the item count in `buy`.

<br>
The following values are required:

- `buy`
- `sell`

The default values are:

|        Name         |  Default value  |
|:-------------------:|:---------------:|
|       `buyB`        |       Air       |
|       `uses`        |        0        |
|      `maxUses`      |        4        |
|     `rewardExp`     |      false      |
|        `xp`         |        0        |
|  `priceMultiplier`  |       0.0       |
|   `specialPrice`    |        0        |
|      `demand`       |        0        |

### Where to put it in?
You use a data pack to provide these files. These are located at `<modid>/merchant_offers/`. An example can be found
[here](https://github.com/MelanX/DataTrader/tree/1.19.x/src/main/resources/data/datatrader/merchant_offers).

### How to use?
You spawn the trader using the `/summon` command, or by using the spawn egg. After this, you use the command
`/datatrader setOffer @e <modid>:<path>` to set the recipe. This can also be done by datapacks.
For a normal trader, I recommend setting `NoAI` to `true`.