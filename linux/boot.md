# Boot

## Grub Boot

Boot can be in MBR or UEFI mode.

If grub is not installed, install it with `grub2-install /dev/sda`.
When changing grub2 options in /etc/default/grub, recreate grub config by running

`grub2-mkconfig -o /boot/grub2/grub.cfg`

### UEFI

UEFI boot requires a /boot/efi partition.
UEFI partition is vfat, 500MB, mounted at /boot/efi as recommended by openSuse installer.

Configuration:
- yast -> boot loader
- efibootmgr

## Recovery

To mount a drive from rescue USB, see [here](https://doc.opensuse.org/documentation/leap/startup/html/book.opensuse.startup/cha.trouble.html#sec.trouble.data.recover.rescue).

Also see [this](https://www.pks.mpg.de/~mueller/docs/suse10.2/html/opensuse-manual_en/manual/sec.trouble.boot.html) for boot troubleshooting.
