#!/bin/sh
sudo apt install -y python3-dev python3-venv
python3 -m venv env
./env/bin/pip3 install -r requirements.txt
echo "[target]\nserver = " > config.ini
