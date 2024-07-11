# Cadmus
*The config values on this page can be found in `config/skyblockbuilder/cadmus.json5` when
[Cadmus 🔗](https://modrinth.com/mod/cadmus) is installed*

## Display Name
This is a component config for the display name that will be shown as owner of the claimed chunks at spawn.
It looks like this:
```json
{
  "text": "SkyblockBuilder Spawn"
}
```
or this, with an additional resource pack where it defines this translation key:
```json
{
  "translate": "cavestone.cadmus.chunk_claim_name"
}
```

## Protect spawn chunks
This setting will automatically claim spawn chunks as admin claims. The radius of protected chunks is defined by 
[`spawnProtectionRadius`](../spawn.md#spawn-protection-radius).
