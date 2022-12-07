sudo ./create_partition.sh sdb 0 1024
sudo debootstrap RELEASE /mnt http://archive.ubuntu.com/ubuntu
cd /usr/share/debootstrap/scripts && ln -sf gutsy jammy
sudo cp /etc/network/interfaces /mnt/etc/network/interfaces
sudo apt-get install arch-install-scripts
genfstab /mnt > /mnt/etc/fstab
sudo apt-get install arch-install-scripts
sudo arch-chroot /mnt
sudo mount --bind /dev /mnt/dev
sudo mount -t proc none /mnt/proc
sudo mount -t sysfs sys /mnt/sys
sudo chroot /mnt /bin/bash
sudo useradd user
sudo passwd  <<< user:password
echo AAAAA > /etc/hostname
dpkg-reconfigure tzdata
apt-get install locales
dpkg-reconfigure locales
apt-get install linux-image-generic
apt-get install grub-pc
apt-get install grub-efi
grub-install /dev/sdb
update-grub
apt-get install firefox
apt-get install wicds