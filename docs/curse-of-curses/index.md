# Curse of Curses
[![](https://cf.way2muchnoise.eu/382881.svg?badge_style=flat)](https://www.curseforge.com/minecraft/mc-mods/curse-of-curses)
[![](https://img.shields.io/modrinth/dt/curse-of-curses?color=00AF5C&label=%E3%85%A4&logo=modrinth&style=flat-square)](https://modrinth.com/mod/curse-of-curses)
[![](https://img.shields.io/github/issues-raw/MelanX/curse-of-curses?style=flat-square)](https://github.com/MelanX/curse-of-curses)


### Config
This mod adds an additional layer of challenge and unpredictability to gameplay. It applies random curses to random 
items on random times to the player. For adjusting the chance, please use the config file. 


### Danger times
You can set the number of "danger times" during a Minecraft day when curses can be applied. By default, there are 3 
danger times between ticks 18000 and 21000. At these specified ticks, each player has a chance to receive curses based 
on the configured probability. The default chance is 1% for each item, and the curses will continue to be applied to 
multiple items unless configured otherwise.


### Cursed Items
Curse of Curses not only applies curses to normal items but also to already cursed items. If there is no matching curse 
available for a particular item, it will not receive an additional curse.


### Cursed Sleep
For players who wish to escape the curses, Curse of Curses includes a feature that applies curses while sleeping. By 
default, this feature is enabled. If you only want to punish players who sleep multiple times, you can set a row count, 
and curses will only be applied after a specific number of sleeps.


### Denylisted Curses
If there are specific curses that you do not want to be applied by this mod, you can use the `denylistedCurses` option in 
the config file. Simply add the curses you want to ignore to the denylist. For example:

- `"minecraft:*"` -> ignores all curses added by Minecraft
- `"minecraft:binding_curse"` -> ignores Curse of Binding

Feel free to customize these configuration options to suit your desired gameplay experience.

