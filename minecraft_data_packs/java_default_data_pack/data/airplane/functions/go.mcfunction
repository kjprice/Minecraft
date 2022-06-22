scoreboard objectives add airplane_count dummy
scoreboard players set @a airplane_count 0

function airplane:loop_run_before
function airplane:loop_run

say Loop started. To stop, run function airplane:loop_stop