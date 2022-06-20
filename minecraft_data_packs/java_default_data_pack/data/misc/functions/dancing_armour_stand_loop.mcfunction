kill @e[type=minecraft:armor_stand]
execute as @p[scores={dancing_armour_count=0}] run say Running step 1
execute as @p[scores={dancing_armour_count=1}] run summon minecraft:armor_stand ~ ~ ~5 {ShowArms:1b}

execute as @p[scores={dancing_armour_count=1}] run say Running step 2
execute as @p[scores={dancing_armour_count=2}] run summon minecraft:armor_stand ~ ~ ~5 {ShowArms:0b}

execute as @p[scores={dancing_armour_count=2}] run say Running step 3
execute as @p[scores={dancing_armour_count=3}] run summon minecraft:armor_stand ~ ~ ~5 {ShowArms:1b}

# Increment score
scoreboard players add @a dancing_armour_count 1

# Run again
execute as @p[scores={dancing_armour_count=..3}] run schedule function misc:dancing_armour_stand_loop 3s
execute as @p[scores={dancing_armour_count=3}] run say All Done!