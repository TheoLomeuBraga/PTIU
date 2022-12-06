#!/bin/bash
#install basics
sudo apt update
sudo apt install python3-pip
sudo apt install python3-tk
apt-get install python-parted

python3 -m pip install tkinter
python3 -m pip install psutil
python3 -m pip install pyudev
python3 -m pip install pyparted


sudo apt-get install x11-xkb-utils
sudo apt install software-properties-common gparted 
sudo add-apt-repository universe
sudo apt update
sudo apt install -y debootstrap arch-install-scripts


#get layouts
rm layouts/base.txt
touch layouts/base.txt
localectl list-x11-keymap-layouts >> layouts/base.txt

rm -r layouts/variants
mkdir layouts/variants

while IFS= read -r line; do
    touch layouts/variants/${line}.txt
    localectl list-x11-keymap-variants ${line} >> layouts/variants/${line}.txt
done < layouts/base.txt

#get locales
rm locales/locales.txt
touch locales/locales.txt
cat /usr/share/i18n/SUPPORTED >> locales/locales.txt




#run
