#!/usr/bin/env bash

if [ -f bin/install_nodejs ]; then
    echo "-----> Running install_nodejs"
    chmod +x bin/install_nodejs
    bin/install_nodejs


    if [ -f bin/install_yuglify ]; then
        echo "-----> Running install_yuglify"
        chmod +x bin/install_yuglify
        bin/install_yuglify
    fi

fi

