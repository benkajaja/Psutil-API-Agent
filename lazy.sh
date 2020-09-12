sudo apt install python3-venv
python3 -m venv env
./env/bin/pip3 install -r requirements.txt
echo "[target]\nserver = " > config.ini
