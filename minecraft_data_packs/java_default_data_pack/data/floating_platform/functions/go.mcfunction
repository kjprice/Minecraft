scoreboard objectives add floating_platform_count dummy
scoreboard players set @a floating_platform_count 0

function floating_platform:loop_run_before
function floating_platform:loop_run

say Loop started. To stop, run function floating_platform:loop_stop