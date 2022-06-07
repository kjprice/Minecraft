# Building epic trains
tp @p ~ ~ ~ facing ~5 ~ ~
function reset_build
kill @e[type=minecart]
setblock ~-1 ~ ~ stone
fill ~0 63 ~0 ~20 63 ~0 redstone_block 
fill ~0 64 ~0 ~20 64 ~0 golden_rail 
ride @p summon_ride minecart