#!/usr/bin/bash
cd "$(dirname "$0")"
cd ..

# nodemon -e py -x 'python -m python.shapes.triangle_stairs'
# nodemon -e py -x 'python -m python.main'
python -m python.main
