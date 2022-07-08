#!/usr/bin/bash
cd "$(dirname "$0")"
cd ..

src_directory=./minecraft_behavior_packs/first_behavior_pack/structures

destinations=( \
    # Microsoft localstate (to test the pack)
    /c/Users/kjpri/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/first_behavior_pack/structures/ \
    # Minecraft server (to test the pack)
    # /c/Users/kjpri/Projects/Minecraft/minecraft_behavior_packs/minecraft_servers/bedrock-server-dev/development_behavior_packs/ \
)

for dest_link in "${destinations[@]}"
do
    cp -r $src_directory/* $dest_link
done