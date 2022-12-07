#!/bin/bash

device="/dev/"$1
home_size_mb=$(($2))
swap_size_mb=$(($3+1))

bios_size_mb=$((500))

begin_bios_mb=$((1))
end_bios_mb=$(($begin_bios_mb+$bios_size_mb+1))

begin_swap_mb=$(($end_bios_mb))
end_swap_mb=$(($begin_swap_mb+$swap_size_mb+1))

begin_home_mb=$(($end_swap_mb+1))
end_home_mb=$(($begin_home_mb+$home_size_mb+1))

if home_size_mb -gt 0
then
echo "with home partition"

sudo parted $device -s mklabel gpt

sudo parted $device -s mkpart EFI fat32 ${begin_bios_mb}MB ${end_bios_mb}MB
sudo mkfs.vfat -F 32 ${device}1

sudo parted $device -s mkpart swap linux-swap ${begin_swap_mb}MB ${end_swap_mb}MB
sudo mkswap ${device}2

sudo parted $device -s mkpart home linux-swap ${begin_home_mb}MB ${end_home_mb}MB
sudo mkfs -t ext4 ${device}3

sudo parted $device -s mkpart main ext4 ${end_home_mb}MB 100%
sudo mkfs -t ext4 ${device}4

sudo mount ${device}4 /mnt

sudo mkdir /mnt/boot
sudo mkdir /mnt/boot/efi
sudo mount ${device}1 /mnt/boot/efi

sudo mkdir /mnt/home
sudo mount ${device}3 /mnt/home

else
echo "no home partition"
sudo parted $device -s mklabel gpt

sudo parted $device -s mkpart EFI fat32 ${begin_bios_mb}MB ${end_bios_mb}MB
sudo mkfs.vfat -F 32 ${device}1

sudo parted $device -s mkpart swap linux-swap ${begin_swap_mb}MB ${end_swap_mb}MB
sudo mkswap ${device}2

sudo parted $device -s mkpart main ext4 ${end_swap_mb}MB 100%
sudo mkfs -t ext4 ${device}3

sudo mount ${device}3 /mnt

sudo mkdir /mnt/boot
sudo mkdir /mnt/boot/efi
sudo mount ${device}1 /mnt/boot/efi



fi
