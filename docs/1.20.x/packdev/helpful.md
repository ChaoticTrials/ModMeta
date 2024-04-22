# Helpful information
## Commands
### Generate Command

To debug your templates, you can use the `/skyblock generate <template name> [pos] [border] [spreads]` command.

Explained:
- `<template name>` is the required name of the fully configured template name, set in 
  [`templates.json5` file](packdev.md#configuring-templates)
- `[pos]` is the optional position where to generate the structure
- `[border]` is `true` or `false`. If this is true, the border configured as `surroundingBlocks` will be added
- `[spreads]` is `true` or `false`. If this is true, the spread structures will also be generated

If `pos` isn't defined, your current position will be used. `border` and `spreads` is `false` as default.