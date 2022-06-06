
src_directory=./minecraft_resource_packs/collage_resource_pack
# src_directory=./minecraft_resource_packs/basic_resource_pack

destinations=( \
    # Microsoft localstate (to test the pack)
    /c/Users/kjpri/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_resource_packs/basic_resource_pack \
    # Minecraft server (to test the pack)
    # /c/Users/kjpri/Projects/Minecraft/minecraft_behavior_packs/minecraft_servers/bedrock-server-dev/development_behavior_packs/ \
)

for dest in "${destinations[@]}"
do
    rm -r $dest/*
    cp -r $src_directory/* $dest
done