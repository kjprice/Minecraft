
src_directory=java_default_data_pack

destinations=( \
    ~/AppData/Roaming/.minecraft/saves/Cheats/datapacks/ \
)

for dest in "${destinations[@]}"
do
    rm -rf $dest/$src_directory/*
    cp -r ./minecraft_data_packs/$src_directory $dest/
done