#!/bin/bash

sudo apt update
sudo apt install python3-pip
sudo apt install python3-tk
python3 -m pip install tkinter
python3 -m pip install psutil

sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update
sudo apt install -y debootstrap arch-install-scripts