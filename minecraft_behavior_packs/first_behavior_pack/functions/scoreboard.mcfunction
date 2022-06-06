# Creates a "test" objective
scoreboard objectives add test dummy test

# Adds one score to the closest player
scoreboard players add @p test 1

# Gives all players (with one test objective) a diamond
give @a[scores={test=1}] diamond