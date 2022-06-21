
# Run before each loop
execute at @p run fill ~-1 ~-1 ~-1 ~1 ~-2 ~1 air replace stone

# Run once each loop
execute at @p[scores={floating_platform_count=0}] run execute at @p run fill ~ ~-1 ~ ~ ~-1 ~ stone


# Increment score
scoreboard players add @a floating_platform_count 1

# Run again
execute at @p[scores={floating_platform_count=..1}] run schedule function floating_platform:loop_run 1t

# Start over when finished
execute at @p[scores={floating_platform_count=1}] run scoreboard players set @a floating_platform_count 0

# Run after each loop
