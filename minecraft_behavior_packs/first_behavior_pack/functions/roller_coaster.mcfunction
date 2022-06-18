# Building epic trains
tp @p ~ ~ ~ facing ~5 ~ ~
function reset_build
fill ~10 63 ~-10 ~30 73 ~10 stone 
fill ~10 73 ~-30 ~30 83 ~-10 stone 
kill @e[type=minecart]
setblock ~-1 ~ ~ stone
ride @p summon_ride minecart
# East: 2
fill ~0 63 ~0 ~1 63 ~0 redstone_block 
fill ~0 64 ~0 ~1 64 ~0 golden_rail 
fill ~0 65 ~0 ~1 65 ~0 air 
fill ~0 66 ~0 ~1 66 ~0 air 
# East: 20
fill ~2 64 ~0 ~2 64 ~0 redstone_block 
fill ~2 65 ~0 ~2 65 ~0 golden_rail 
fill ~2 66 ~0 ~2 66 ~0 air 
fill ~2 67 ~0 ~2 67 ~0 air 
fill ~3 65 ~0 ~3 65 ~0 redstone_block 
fill ~3 66 ~0 ~3 66 ~0 golden_rail 
fill ~3 67 ~0 ~3 67 ~0 air 
fill ~3 68 ~0 ~3 68 ~0 air 
fill ~4 66 ~0 ~4 66 ~0 redstone_block 
fill ~4 67 ~0 ~4 67 ~0 golden_rail 
fill ~4 68 ~0 ~4 68 ~0 air 
fill ~4 69 ~0 ~4 69 ~0 air 
fill ~5 67 ~0 ~5 67 ~0 redstone_block 
fill ~5 68 ~0 ~5 68 ~0 golden_rail 
fill ~5 69 ~0 ~5 69 ~0 air 
fill ~5 70 ~0 ~5 70 ~0 air 
fill ~6 68 ~0 ~6 68 ~0 redstone_block 
fill ~6 69 ~0 ~6 69 ~0 golden_rail 
fill ~6 70 ~0 ~6 70 ~0 air 
fill ~6 71 ~0 ~6 71 ~0 air 
fill ~7 69 ~0 ~7 69 ~0 redstone_block 
fill ~7 70 ~0 ~7 70 ~0 golden_rail 
fill ~7 71 ~0 ~7 71 ~0 air 
fill ~7 72 ~0 ~7 72 ~0 air 
fill ~8 70 ~0 ~8 70 ~0 redstone_block 
fill ~8 71 ~0 ~8 71 ~0 golden_rail 
fill ~8 72 ~0 ~8 72 ~0 air 
fill ~8 73 ~0 ~8 73 ~0 air 
fill ~9 71 ~0 ~9 71 ~0 redstone_block 
fill ~9 72 ~0 ~9 72 ~0 golden_rail 
fill ~9 73 ~0 ~9 73 ~0 air 
fill ~9 74 ~0 ~9 74 ~0 air 
fill ~10 72 ~0 ~10 72 ~0 redstone_block 
fill ~10 73 ~0 ~10 73 ~0 golden_rail 
fill ~10 74 ~0 ~10 74 ~0 air 
fill ~10 75 ~0 ~10 75 ~0 air 
fill ~11 73 ~0 ~11 73 ~0 redstone_block 
fill ~11 74 ~0 ~11 74 ~0 golden_rail 
fill ~11 75 ~0 ~11 75 ~0 air 
fill ~11 76 ~0 ~11 76 ~0 air 
fill ~12 74 ~0 ~12 74 ~0 redstone_block 
fill ~12 75 ~0 ~12 75 ~0 golden_rail 
fill ~12 76 ~0 ~12 76 ~0 air 
fill ~12 77 ~0 ~12 77 ~0 air 
fill ~13 75 ~0 ~13 75 ~0 redstone_block 
fill ~13 76 ~0 ~13 76 ~0 golden_rail 
fill ~13 77 ~0 ~13 77 ~0 air 
fill ~13 78 ~0 ~13 78 ~0 air 
fill ~14 76 ~0 ~14 76 ~0 redstone_block 
fill ~14 77 ~0 ~14 77 ~0 golden_rail 
fill ~14 78 ~0 ~14 78 ~0 air 
fill ~14 79 ~0 ~14 79 ~0 air 
fill ~15 77 ~0 ~15 77 ~0 redstone_block 
fill ~15 78 ~0 ~15 78 ~0 golden_rail 
fill ~15 79 ~0 ~15 79 ~0 air 
fill ~15 80 ~0 ~15 80 ~0 air 
fill ~16 78 ~0 ~16 78 ~0 redstone_block 
fill ~16 79 ~0 ~16 79 ~0 golden_rail 
fill ~16 80 ~0 ~16 80 ~0 air 
fill ~16 81 ~0 ~16 81 ~0 air 
fill ~17 79 ~0 ~17 79 ~0 redstone_block 
fill ~17 80 ~0 ~17 80 ~0 golden_rail 
fill ~17 81 ~0 ~17 81 ~0 air 
fill ~17 82 ~0 ~17 82 ~0 air 
fill ~18 80 ~0 ~18 80 ~0 redstone_block 
fill ~18 81 ~0 ~18 81 ~0 golden_rail 
fill ~18 82 ~0 ~18 82 ~0 air 
fill ~18 83 ~0 ~18 83 ~0 air 
fill ~19 81 ~0 ~19 81 ~0 redstone_block 
fill ~19 82 ~0 ~19 82 ~0 golden_rail 
fill ~19 83 ~0 ~19 83 ~0 air 
fill ~19 84 ~0 ~19 84 ~0 air 
fill ~20 82 ~0 ~20 82 ~0 redstone_block 
fill ~20 83 ~0 ~20 83 ~0 golden_rail 
fill ~20 84 ~0 ~20 84 ~0 air 
fill ~20 85 ~0 ~20 85 ~0 air 
fill ~21 83 ~0 ~21 83 ~0 redstone_block 
fill ~21 84 ~0 ~21 84 ~0 golden_rail 
fill ~21 85 ~0 ~21 85 ~0 air 
fill ~21 86 ~0 ~21 86 ~0 air 
# North: 15
fill ~21 83 ~-1 ~21 83 ~-15 redstone_block 
fill ~21 84 ~-1 ~21 84 ~-15 golden_rail 
fill ~21 85 ~-1 ~21 85 ~-15 air 
fill ~21 86 ~-1 ~21 86 ~-15 air 
setblock ~21 84 ~0 rail
# West: 1
fill ~20 83 ~-15 ~20 83 ~-15 redstone_block 
fill ~20 84 ~-15 ~20 84 ~-15 golden_rail 
fill ~20 85 ~-15 ~20 85 ~-15 air 
fill ~20 86 ~-15 ~20 86 ~-15 air 
setblock ~21 84 ~-15 rail
# West: 5
fill ~19 82 ~-15 ~19 82 ~-15 redstone_block 
fill ~19 83 ~-15 ~19 83 ~-15 golden_rail 
fill ~19 84 ~-15 ~19 84 ~-15 air 
fill ~19 85 ~-15 ~19 85 ~-15 air 
fill ~18 81 ~-15 ~18 81 ~-15 redstone_block 
fill ~18 82 ~-15 ~18 82 ~-15 golden_rail 
fill ~18 83 ~-15 ~18 83 ~-15 air 
fill ~18 84 ~-15 ~18 84 ~-15 air 
fill ~17 80 ~-15 ~17 80 ~-15 redstone_block 
fill ~17 81 ~-15 ~17 81 ~-15 golden_rail 
fill ~17 82 ~-15 ~17 82 ~-15 air 
fill ~17 83 ~-15 ~17 83 ~-15 air 
fill ~16 79 ~-15 ~16 79 ~-15 redstone_block 
fill ~16 80 ~-15 ~16 80 ~-15 golden_rail 
fill ~16 81 ~-15 ~16 81 ~-15 air 
fill ~16 82 ~-15 ~16 82 ~-15 air 
fill ~15 78 ~-15 ~15 78 ~-15 redstone_block 
fill ~15 79 ~-15 ~15 79 ~-15 golden_rail 
fill ~15 80 ~-15 ~15 80 ~-15 air 
fill ~15 81 ~-15 ~15 81 ~-15 air 
# North: 5
fill ~15 78 ~-16 ~15 78 ~-20 redstone_block 
fill ~15 79 ~-16 ~15 79 ~-20 golden_rail 
fill ~15 80 ~-16 ~15 80 ~-20 air 
fill ~15 81 ~-16 ~15 81 ~-20 air 
setblock ~15 79 ~-15 rail
# West: 1
fill ~14 78 ~-20 ~14 78 ~-20 redstone_block 
fill ~14 79 ~-20 ~14 79 ~-20 golden_rail 
fill ~14 80 ~-20 ~14 80 ~-20 air 
fill ~14 81 ~-20 ~14 81 ~-20 air 
setblock ~15 79 ~-20 rail
# West: 2
fill ~13 79 ~-20 ~13 79 ~-20 redstone_block 
fill ~13 80 ~-20 ~13 80 ~-20 golden_rail 
fill ~13 81 ~-20 ~13 81 ~-20 air 
fill ~13 82 ~-20 ~13 82 ~-20 air 
fill ~12 80 ~-20 ~12 80 ~-20 redstone_block 
fill ~12 81 ~-20 ~12 81 ~-20 golden_rail 
fill ~12 82 ~-20 ~12 82 ~-20 air 
fill ~12 83 ~-20 ~12 83 ~-20 air 
function 