
src_directory=./minecraft_behavior_packs/first_behavior_pack/functions

destinations=( \
    # Microsoft localstate (to test the pack)
    /c/Users/kjpri/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/first_behavior_pack/functions/ \
    # Minecraft server (to test the pack)
    # /c/Users/kjpri/Projects/Minecraft/minecraft_behavior_packs/minecraft_servers/bedrock-server-dev/development_behavior_packs/ \
)

for dest_link in "${destinations[@]}"
do
    time cp -r $src_directory/* $dest_link
done