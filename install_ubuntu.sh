sudo sh install_dependences.sh

#copy to /usr/share
sudo rm -r /usr/share/technomancy_instaler
sudo cp -t ./ /usr/share

#change name to technomancy_instaler
sudo cd /usr/share 
sudo mv PTIU technomancy_instaler
sudo cd -

#
sudo touch /usr/share/applications/technomancy_instaler.desktop
echo "[Desktop Entry]" >> /usr/share/applications/technomancy_instaler.desktop
echo "Encoding=UTF-8" >> /usr/share/applications/technomancy_instaler.desktop
echo "Version=1.0" >> /usr/share/applications/technomancy_instaler.desktop
echo "Type=Application" >> /usr/share/applications/technomancy_instaler.desktop
echo "Terminal=true" >> /usr/share/applications/technomancy_instaler.desktop
echo "Exec=sh /usr/share/technomancy_instaler/un.sh" >> /usr/share/applications/technomancy_instaler.desktop
echo "Path=/usr/share/technomancy_instaler/" >> /usr/share/applications/technomancy_instaler.desktop
echo "Type=Application" >> /usr/share/applications/technomancy_instaler.desktop
echo "Name=technomancy instaler center" >> /usr/share/applications/technomancy_instaler.desktop
echo "Icon=/usr/share/technomancy_instaler/install_icon.png" >> /usr/share/applications/technomancy_instaler.desktop





