sudo sh install_dependences.sh

sudo rm -r /usr/share/technomancy_instaler

sudo cp -t ./ /usr/share


echo "[Desktop Entry]" >> /usr/share/applications/openbox_config_center.desktop
echo "Encoding=UTF-8" >> /usr/share/applications/openbox_config_center.desktop
echo "Version=1.0" >> /usr/share/applications/openbox_config_center.desktop
echo "Type=Application" >> /usr/share/applications/openbox_config_center.desktop
echo "Terminal=false" >> /usr/share/applications/openbox_config_center.desktop
echo "Exec=python3 /usr/share/openbox_config_center/center.py" >> /usr/share/applications/openbox_config_center.desktop
echo "Path=/usr/share/openbox_config_center/" >> /usr/share/applications/openbox_config_center.desktop
echo "Type=Application" >> /usr/share/applications/openbox_config_center.desktop
echo "Name=openbox configurations center" >> /usr/share/applications/openbox_config_center.desktop
echo "Icon=/usr/share/openbox_config_center/config_icon.png" >> /usr/share/applications/openbox_config_center.desktop





