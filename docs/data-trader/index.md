# Data Trader
[![](https://cf.way2muchnoise.eu/650573.svg?badge_style=flat)](https://www.curseforge.com/minecraft/mc-mods/data-trader) [![](https://img.shields.io/badge/dynamic/json?color=5da545&label=&labelColor=383838&prefix=%20&query=downloads&url=https://api.modrinth.com/api/v1/mod/No1xZeN1&style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSIgd2lkdGg9IjE0LjY2NyIgaGVpZ2h0PSIxNC42NjciICB4bWxuczp2PSJodHRwczovL3ZlY3RhLmlvL25hbm8iPjxkZWZzPjxjbGlwUGF0aCBpZD0iQSI+PHBhdGggZD0iTTAgMGgxMXYxMUgweiIvPjwvY2xpcFBhdGg+PC9kZWZzPjxnIGNsaXAtcGF0aD0idXJsKCNBKSI+PHBhdGggZD0iTTEuMzA5IDcuODU3YTQuNjQgNC42NCAwIDAgMS0uNDYxLTEuMDYzSDBDLjU5MSA5LjIwNiAyLjc5NiAxMSA1LjQyMiAxMWMxLjk4MSAwIDMuNzIyLTEuMDIgNC43MTEtMi41NTZoMGwtLjc1LS4zNDVjLS44NTQgMS4yNjEtMi4zMSAyLjA5Mi0zLjk2MSAyLjA5MmE0Ljc4IDQuNzggMCAwIDEtMy4wMDUtMS4wNTVsMS44MDktMS40NzQuOTg0Ljg0NyAxLjkwNS0xLjAwM0w4LjE3NCA1LjgybC0uMzg0LS43ODYtMS4xMTYuNjM1LS41MTYuNjk0LS42MjYuMjM2LS44NzMtLjM4N2gwbC0uMjEzLS45MS4zNTUtLjU2Ljc4Ny0uMzcuODQ1LS45NTktLjcwMi0uNTEtMS44NzQuNzEzLTEuMzYyIDEuNjUxLjY0NSAxLjA5OC0xLjgzMSAxLjQ5MnptOS42MTQtMS40NEE1LjQ0IDUuNDQgMCAwIDAgMTEgNS41QzExIDIuNDY0IDguNTAxIDAgNS40MjIgMCAyLjc5NiAwIC41OTEgMS43OTQgMCA0LjIwNmguODQ4QzEuNDE5IDIuMjQ1IDMuMjUyLjgwOSA1LjQyMi44MDljMi42MjYgMCA0Ljc1OCAyLjEwMiA0Ljc1OCA0LjY5MSAwIC4xOS0uMDEyLjM3Ni0uMDM0LjU2bC43NzcuMzU3aDB6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGZpbGw9IiM1ZGE0MjYiLz48L2c+PC9zdmc+)](https://modrinth.com/mod/data-trader) [![](https://img.shields.io/github/issues-raw/MelanX/DataTrader?style=flat-square)](https://github.com/MelanX/DataTrader)

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