#!/bin/sh

set -e

./bin/coverage run \
    --source src/yafowil/widget/wysihtml5 \
    --omit src/yafowil/widget/wysihtml5/example.py \
    -m yafowil.widget.wysihtml5.tests
./bin/coverage report
./bin/coverage html
