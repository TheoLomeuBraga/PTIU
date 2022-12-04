#!/bin/bash
#install basics
sudo sh install-basics.sh

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
sudo python3 ptiu-gui.py