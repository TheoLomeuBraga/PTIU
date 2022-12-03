#!/bin/bash
sudo apt update
sudo apt install python3-pip
python3 -m pip install pysimplegui
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update
sudo apt install -y debootstrap arch-install-scripts