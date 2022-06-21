# Always face player
execute at @e[tag=dancing_armour] run tp @e[tag=dancing_armour] ~ ~ ~ facing entity @p
schedule function dancing_armor_stand:dancing_armour_stand_face_player 1t