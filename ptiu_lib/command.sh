sudo ./create_partition.sh sdb 0 1024
sudo debootstrap --arch=amd64 --variant=minbase focal /mnt https://mirror.leaseweb.com/ubuntu/
sudo cd /usr/share/debootstrap/scripts && ln -sf gutsy jammy
sudo yes | sudo cp -rf ./resolv.conf /mnt/etc/
sudo yes | sudo cp -rf ./sources.list /mnt/etc/apt/
genfstab /mnt > /mnt/etc/fstab
sudo mount --bind /dev /mnt/dev
sudo mount -t proc none /mnt/proc
sudo mount -t sysfs sys /mnt/sys
sudo chroot /mnt << EOF
deb http://us.archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb http://us.archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb http://us.archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://us.archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
useradd -m -d /home/user user
echo "user:password" | chpasswd
echo AAAAA > /etc/hostname
apt-get update
apt -y install locales
apt -y install grub-efi
apt -y install grub-pc
apt -y install grub-common
apt -y install grub-pc-bin
apt -y install grub-efi-amd64-bin
apt -y install linux-image-generic
apt -y install plymouth-x11
apt -y install xinput
apt -y install software-properties-common
apt -y install software-properties-common
add-apt-repository ppa:nilarimogard/webupd8
add-apt-repository ppa:noobslab/mint
apt update
apt -y install universe
apt -y install network-manager
apt -y install xfce4
apt -y install firefox
apt -y install xorg
apt -y install mdm
apt -y install mdm-themes
dpkg-reconfigure tzdata
dpkg-reconfigure locales
grub-install /dev/sdb
grub-install --target=x86_64-efi /dev/sdb --force
grub-install --target=x86_64-efi --efi-directory=/boot /dev/sdb --force
grub-install --target=x86_64-efi --efi-directory=/boot/EFI /dev/sdb --force
grub-install --target=i386-pc /dev/sdb --force
update-grub
plymouth message --text="made with PTIU"
dpkg-reconfigure mdm
chsh -s /bin/bash
chsh -s /bin/bash user
apt -y install sudo
usermod -aG sudo user
