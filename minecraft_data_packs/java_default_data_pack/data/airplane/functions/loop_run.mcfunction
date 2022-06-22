
# Run before each loop
execute at @p run fill ~-1 ~-1 ~-1 ~1 ~-2 ~1 air replace stone
execute at @p[y_rotation=-46..45] run tp @p ~ ~ ~1
execute at @p[y_rotation=46..135] run tp @p ~-1 ~ ~
execute at @p[y_rotation=136..225] run tp @p ~ ~ ~-1
execute at @p[y_rotation=226..-46] run tp @p ~1 ~ ~

# Run once each loop
execute at @p[scores={airplane_count=0}] run execute at @p run fill ~ ~-1 ~ ~ ~-1 ~ stone


# Increment score
scoreboard players add @a airplane_count 1

# Run again
execute at @p[scores={airplane_count=..1}] run schedule function airplane:loop_run 1t

# Start over when finished
execute at @p[scores={airplane_count=1}] run scoreboard players set @a airplane_count 0

# Run after each loop
