@echo off
python -m venv ./venv
./venv/bin/pip install -r ./requirements.txt
./venv/bin/pip install PyAudio