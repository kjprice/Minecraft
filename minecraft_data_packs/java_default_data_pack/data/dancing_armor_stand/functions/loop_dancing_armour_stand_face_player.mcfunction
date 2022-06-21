# Always face player
execute at @e[tag=tag_dancing_armor_stand] run tp @e[tag=tag_dancing_armor_stand] ~ ~ ~ facing entity @p
schedule function dancing_armor_stand:loop_dancing_armour_stand_face_player 1t