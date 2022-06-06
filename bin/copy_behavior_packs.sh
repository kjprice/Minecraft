
src_directory=./minecraft_behavior_packs/collage_behavior_pack
# src_directory=./minecraft_behavior_packs/basic_behavior_pack

destinations=( \
    # Microsoft localstate (to test the pack)
    /c/Users/kjpri/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/basic_behavior_pack \
    # Minecraft server (to test the pack)
    # /c/Users/kjpri/Projects/Minecraft/minecraft_behavior_packs/minecraft_servers/bedrock-server-dev/development_behavior_packs/ \
)

for dest in "${destinations[@]}"
do
    rm -r $dest/*
    cp -r $src_directory/* $dest
done