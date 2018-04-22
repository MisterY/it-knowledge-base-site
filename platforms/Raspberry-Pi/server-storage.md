# Storage

## Hardware

It is recommended to use a powered USB hub to which the storage devices are to be attached.

- USB stick for fast memory
- HDD 2.5" for large memory storage. Power down after timeout when not in use.

Commands:

- lsblk
- fdisk -l
- df

### Automount

Set up automount points with fstab. Run `sudo blkid` to get the partition id.

Set the user and group ids to the current user. Find out the ids with `id -u <user>` and `id -g <user>` or simply use the name (uid=<username>,gid=<username>).

Links:

- auto-mount USB Hard Drive on Raspberry Pi ([link](https://gist.github.com/etes/aa76a6e9c80579872e5f))

### USB Stick

`lsusb` displays all attached USB devices. The commands above show drives and partitions.
Create a directory in /mnt (i.e. /mnt/usb) and mount the drive there.

- RPi mounting USB drive [link](https://elinux.org/RPi_Adding_USB_Drives)
