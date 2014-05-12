#!/usr/bin/env bash

env="env"

if [ ! -d "$env" ]; then
    virtualenv "$env"
    ln -s "$env/bin/activate" "activate"
fi

source activate

pip install --upgrade -r requirements.txt
