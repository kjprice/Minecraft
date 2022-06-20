kill @e[type=minecraft:armor_stand]
execute at @p[scores={dancing_armour_count=0}] run say Running step 1
execute at @p[scores={dancing_armour_count=0}] run summon minecraft:armor_stand ~ ~ ~2 {ShowArms:1b}

execute at @p[scores={dancing_armour_count=1}] run say Running step 2
execute at @p[scores={dancing_armour_count=1}] run summon minecraft:armor_stand ~ ~ ~2 {ShowArms:0b}

execute at @p[scores={dancing_armour_count=2}] run say Running step 3
execute at @p[scores={dancing_armour_count=2}] run summon minecraft:armor_stand ~ ~ ~2 {ShowArms:1b}

# Increment score
scoreboard players add @a dancing_armour_count 1

# Run again
execute at @p[scores={dancing_armour_count=..3}] run schedule function misc:dancing_armour_stand_loop 0.5s
execute at @p[scores={dancing_armour_count=3}] run say All Done!