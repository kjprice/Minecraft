kill @e[type=minecraft:armor_stand]
execute at @p[scores={dancing_armour_count=0}] run say Running step 1
execute at @p[scores={dancing_armour_count=0}] run summon minecraft:armor_stand ~ ~ ~2 {NoBasePlate:1b,ShowArms:1b,Pose:{LeftArm:[0f,0f,0f]}}

execute at @p[scores={dancing_armour_count=1}] run say Running step 2
execute at @p[scores={dancing_armour_count=1}] run summon minecraft:armor_stand ~ ~ ~2 {NoBasePlate:1b,ShowArms:1b,Pose:{LeftArm:[20f,0f,0f]}}

execute at @p[scores={dancing_armour_count=2}] run say Running step 3
execute at @p[scores={dancing_armour_count=2}] run summon minecraft:armor_stand ~ ~ ~2 {NoBasePlate:1b,ShowArms:1b,Pose:{LeftArm:[40f,0f,0f]}}

execute at @p[scores={dancing_armour_count=3}] run say Running step 4
execute at @p[scores={dancing_armour_count=3}] run summon minecraft:armor_stand ~ ~ ~2 {NoBasePlate:1b,ShowArms:1b,Pose:{LeftArm:[60f,0f,0f]}}

execute at @p[scores={dancing_armour_count=4}] run say Running step 5
execute at @p[scores={dancing_armour_count=4}] run summon minecraft:armor_stand ~ ~ ~2 {NoBasePlate:1b,ShowArms:1b,Pose:{LeftArm:[80f,0f,0f]}}

execute at @p[scores={dancing_armour_count=5}] run say Running step 6
execute at @p[scores={dancing_armour_count=5}] run summon minecraft:armor_stand ~ ~ ~2 {NoBasePlate:1b,ShowArms:1b,Pose:{LeftArm:[100f,0f,0f]}}

# Increment score
scoreboard players add @a dancing_armour_count 1

# Run again
execute at @p[scores={dancing_armour_count=..6}] run schedule function misc:dancing_armour_stand_loop 0.5s
execute at @p[scores={dancing_armour_count=6}] run say All Done!