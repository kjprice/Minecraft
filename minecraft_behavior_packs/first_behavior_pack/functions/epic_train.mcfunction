# Building epic trains
tp @p ~ ~ ~ facing ~5 ~ ~
function reset_build
kill @e[type=minecart]
setblock ~-1 ~ ~ stone
ride @p summon_ride minecart
# East: 2
fill ~0 63 ~0 ~1 63 ~0 redstone_block 
fill ~0 64 ~0 ~1 64 ~0 golden_rail 
# North: 2
fill ~1 63 ~-1 ~1 63 ~-2 redstone_block 
fill ~1 64 ~-1 ~1 64 ~-2 golden_rail 
setblock ~1 64 ~0 rail
# West: 1
fill ~0 63 ~-2 ~0 63 ~-2 redstone_block 
fill ~0 64 ~-2 ~0 64 ~-2 golden_rail 
setblock ~1 64 ~-2 rail
# West: 2
fill ~-1 63 ~-2 ~-1 63 ~-2 redstone_block 
fill ~-1 64 ~-2 ~-1 64 ~-2 golden_rail 
fill ~-2 64 ~-2 ~-2 64 ~-2 redstone_block 
fill ~-2 65 ~-2 ~-2 65 ~-2 golden_rail 