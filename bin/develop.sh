#!/usr/bin/bash
cd "$(dirname "$0")"
cd ..

nodemon -e py -x 'sh bin/create_and_copy.sh'


