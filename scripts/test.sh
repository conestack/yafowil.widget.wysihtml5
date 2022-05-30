#!/bin/bash
#
# Run python tests.

function run_tests {
    local target=$1

    if [ -e "$target" ]; then
        ./$target/bin/python -m yafowil.widget.wysihtml5.tests
    else
        echo "Target $target not found."
    fi
}

run_tests py2
run_tests py3
run_tests pypy3
