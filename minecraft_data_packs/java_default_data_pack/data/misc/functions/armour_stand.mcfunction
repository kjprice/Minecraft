kill @e[type=minecraft:armor_stand]
summon minecraft:armor_stand ~-2 ~ ~-2 {NoBasePlate:1b,ShowArms:1b,Tags:["test_armor_stand"]}
data get entity @e[tag=test_armor_stand,limit=1]