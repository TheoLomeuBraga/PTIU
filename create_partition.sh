#!/bin/bash

device="/dev/"$1
home_size_mb=$(($2))
swap_size_mb=$(($3+1))

efi_size_mb=$((500))

boot_size_mb=$((500))

begin_efi_mb=$((1))
end_efi_mb=$(($begin_efi_mb+$efi_size_mb+1))

begin_swap_mb=$(($end_efi_mb))
end_swap_mb=$(($begin_swap_mb+$swap_size_mb+1))

begin_home_mb=$(($end_swap_mb+1))
end_home_mb=$(($begin_home_mb+$home_size_mb+1))

if (($home_size_mb > 0))
then
echo "with home partition"

sudo parted $device -s mklabel gpt

sudo parted $device -s mkpart EFI fat32 ${begin_efi_mb}MB ${end_efi_mb}MB
sudo mkfs.vfat -F 32 ${device}1

sudo parted $device -s mkpart swap linux-swap ${begin_swap_mb}MB ${end_swap_mb}MB
sudo mkswap ${device}2

sudo parted $device -s mkpart home ext4 ${begin_home_mb}MB ${end_home_mb}MB
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

sudo parted $device -s mkpart EFI fat32 ${begin_efi_mb}MB ${end_efi_mb}MB
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
