#!/usr/bin/bash
cd "$(dirname "$0")"

cd ..
pwd
sh bin/run_py.sh
sh bin/copy_functions.sh
sh bin/copy_structures.sh

sh bin/copy_resource_packs.sh
sh bin/copy_behavior_packs.sh
sh bin/copy_data_packs.sh
