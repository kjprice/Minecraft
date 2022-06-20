# TODO: Update
kill @e[tag=dancing_armour]
summon minecraft:armor_stand ~ ~ ~-2 {NoBasePlate:1b,ShowArms:1b,ArmorItems:[{},{},{},{id:diamond_helmet,Count:1}],Tags:["dancing_armour"]}
scoreboard objectives add dancing_armour_count dummy
scoreboard players set @a dancing_armour_count 0