# Building epic trains
tp @p ~ ~ ~ facing ~5 ~ ~
function reset_build
kill @e[type=minecart]
setblock ~-1 ~ ~ stone
ride @p summon_ride minecart
fill ~0 63 ~0 ~10 63 ~0 redstone_block 
fill ~0 64 ~0 ~10 64 ~0 golden_rail 
fill ~10 63 ~0 ~10 63 ~10 redstone_block 
fill ~10 64 ~0 ~10 64 ~10 golden_rail 
setblock ~10 64 ~0 rail
fill ~10 63 ~10 ~5 63 ~10 redstone_block 
fill ~10 64 ~10 ~5 64 ~10 golden_rail 
setblock ~10 64 ~10 rail
fill ~5 63 ~10 ~5 63 ~8 redstone_block 
fill ~5 64 ~10 ~5 64 ~8 golden_rail 
setblock ~5 64 ~10 rail
fill ~5 63 ~8 ~5 63 ~7 redstone_block 
fill ~5 64 ~8 ~5 64 ~7 golden_rail 
fill ~5 64 ~7 ~5 64 ~6 redstone_block 
fill ~5 65 ~7 ~5 65 ~6 golden_rail 